# API Documentation - Sustainability Footprint Agent

Complete API reference for the Sustainability Footprint Agent.

## Base URL

**Local Development**: `http://localhost:8000`  
**Production**: `https://your-deployed-url.com`

## Authentication

Currently, no authentication is required. For production, consider adding API keys.

---

## Endpoints

### 1. Health Check

Check if the agent is running and ready to accept requests.

**Endpoint**: `GET /health`

**Request**: No parameters required

**Response**:
```json
{
  "status": "ok",
  "agent_name": "sustainability-footprint-agent",
  "ready": true
}
```

**Status Codes**:
- `200 OK`: Agent is healthy
- `500 Internal Server Error`: Agent has issues

**Example**:
```bash
curl http://localhost:8000/health
```

---

### 2. Agent Information

Get metadata about the agent including capabilities and supported intents.

**Endpoint**: `GET /`

**Request**: No parameters required

**Response**:
```json
{
  "agent_name": "sustainability-footprint-agent",
  "description": "Sustainability Footprint Agent - Environmental impact analysis and sustainability assessment",
  "version": "1.0.0",
  "endpoints": {
    "main": "/sustainability-footprint-agent",
    "health": "/health"
  },
  "intents": [
    "carbon_footprint_analysis",
    "energy_consumption_tracking",
    "waste_management_assessment",
    "sustainability_metrics",
    "environmental_impact_analysis",
    "green_building_assessment",
    "renewable_energy_recommendations"
  ]
}
```

**Status Codes**:
- `200 OK`: Success

**Example**:
```bash
curl http://localhost:8000/
```

---

### 3. Process Sustainability Query

Main endpoint for processing sustainability-related queries.

**Endpoint**: `POST /sustainability-footprint-agent`

**Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
  "messages": [
    {
      "role": "user" | "assistant" | "system",
      "content": "string"
    }
  ]
}
```

**Request Schema**:
- `messages` (array, required): List of message objects
  - `role` (string, required): One of "user", "assistant", or "system"
  - `content` (string, required): Message content

**Response Body** (Success):
```json
{
  "agent_name": "sustainability-footprint-agent",
  "status": "success",
  "data": {
    "message": "Analysis results and recommendations...",
    "metadata": {
      "source": "generated" | "ltm_cache",
      "query": "Original user query"
    }
  },
  "error_message": null
}
```

**Response Body** (Error):
```json
{
  "agent_name": "sustainability-footprint-agent",
  "status": "error",
  "data": null,
  "error_message": "Description of what went wrong"
}
```

**Status Codes**:
- `200 OK`: Request processed successfully (even if analysis failed)
- `400 Bad Request`: Invalid request format
- `500 Internal Server Error`: Unexpected server error

**Example Requests**:

#### Simple Query
```bash
curl -X POST http://localhost:8000/sustainability-footprint-agent \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is my carbon footprint from driving?"
      }
    ]
  }'
```

#### Multi-Turn Conversation
```bash
curl -X POST http://localhost:8000/sustainability-footprint-agent \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      {
        "role": "user",
        "content": "I want to reduce energy costs."
      },
      {
        "role": "assistant",
        "content": "Great! What type of building?"
      },
      {
        "role": "user",
        "content": "Residential home."
      }
    ]
  }'
```

---

## Data Models

### Message
```typescript
{
  role: "user" | "assistant" | "system"
  content: string
}
```

### AgentRequest
```typescript
{
  messages: Message[]
}
```

### AgentResponse
```typescript
{
  agent_name: string
  status: "success" | "error"
  data: {
    message: string
    metadata: {
      source: "generated" | "ltm_cache"
      query: string
    }
  } | null
  error_message: string | null
}
```

### HealthCheckResponse
```typescript
{
  status: "ok" | "degraded" | "down"
  agent_name: string
  ready: boolean
}
```

---

## Supported Intents

The agent can handle queries related to:

1. **carbon_footprint_analysis**
   - Calculate CO2 emissions
   - Analyze carbon impact
   - Footprint reduction strategies

2. **energy_consumption_tracking**
   - Monitor energy usage
   - Identify inefficiencies
   - Optimization recommendations

3. **waste_management_assessment**
   - Waste reduction strategies
   - Recycling programs
   - Composting guidance

4. **sustainability_metrics**
   - Environmental KPIs
   - Sustainability reporting
   - Impact measurement

5. **environmental_impact_analysis**
   - Comprehensive assessments
   - Lifecycle analysis
   - Environmental reports

6. **green_building_assessment**
   - LEED certification
   - Energy-efficient design
   - Sustainable materials

7. **renewable_energy_recommendations**
   - Solar power analysis
   - Wind energy options
   - ROI calculations

---

## Error Codes

| Error | Status | Description | Solution |
|-------|--------|-------------|----------|
| Empty messages | 400 | No messages in request | Include at least one message |
| Invalid JSON | 400 | Malformed request body | Check JSON syntax |
| Missing role | 400 | Message missing role field | Add "role" field |
| Missing content | 400 | Message missing content | Add "content" field |
| Processing error | 200 | Analysis failed | Check error_message in response |
| Server error | 500 | Unexpected error | Check server logs |

**Important**: The agent always returns valid JSON, even on errors. Check the `status` field to determine success/failure.

---

## Rate Limiting

Currently, no rate limiting is enforced. For production:
- Recommended: 60 requests per minute per IP
- Implement using middleware or API gateway

---

## Timeouts

- **Request timeout**: 30 seconds
- **Agent processing**: 25 seconds maximum
- If exceeded, returns error response

---

## Long-Term Memory (LTM)

The agent caches successful responses for improved performance:

- **Cache key**: MD5 hash of normalized query
- **Storage**: JSON file in `shared/LTM/sustainability-footprint-agent/`
- **Benefits**: 
  - Faster response times
  - Reduced API costs (OpenAI)
  - Consistent answers

**Response Metadata**:
- `source: "generated"` - New analysis performed
- `source: "ltm_cache"` - Retrieved from cache

---

## Example Usage in Different Languages

### Python
```python
import requests

response = requests.post(
    "http://localhost:8000/sustainability-footprint-agent",
    json={
        "messages": [
            {"role": "user", "content": "Calculate carbon footprint"}
        ]
    }
)

result = response.json()
print(result["data"]["message"])
```

### JavaScript (Node.js)
```javascript
const response = await fetch('http://localhost:8000/sustainability-footprint-agent', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    messages: [
      { role: 'user', content: 'Calculate carbon footprint' }
    ]
  })
});

const result = await response.json();
console.log(result.data.message);
```

### cURL
```bash
curl -X POST http://localhost:8000/sustainability-footprint-agent \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Calculate carbon footprint"}]}'
```

### PowerShell
```powershell
$body = @{
    messages = @(
        @{
            role = "user"
            content = "Calculate carbon footprint"
        }
    )
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/sustainability-footprint-agent" `
    -Method Post -Body $body -ContentType "application/json"
```

---

## Best Practices

### 1. Query Optimization
- Be specific in queries for better results
- Include context for multi-turn conversations
- Use clear, concise language

### 2. Error Handling
Always check the `status` field:
```python
if result["status"] == "success":
    print(result["data"]["message"])
else:
    print(f"Error: {result['error_message']}")
```

### 3. Conversation Context
Include conversation history for better context:
```json
{
  "messages": [
    {"role": "assistant", "content": "Previous response"},
    {"role": "user", "content": "Follow-up question"}
  ]
}
```

### 4. Timeout Handling
Implement client-side timeouts:
```python
response = requests.post(url, json=data, timeout=35)
```

---

## CORS Configuration

The agent allows all origins by default:
```python
allow_origins=["*"]
```

For production, restrict to specific domains:
```python
allow_origins=["https://your-frontend.com"]
```

---

## Monitoring

Track these metrics:
- **Response time**: Average time per request
- **Error rate**: Percentage of failed requests
- **Cache hit rate**: LTM effectiveness
- **Query types**: Most common intents

---

## Support

For API issues:
1. Check health endpoint
2. Verify request format
3. Review error messages
4. Check server logs
5. Contact support team

---

## Version History

**v1.0.0** (Current)
- Initial release
- All core intents supported
- LTM caching implemented
- OpenAI integration (optional)

---

**Last Updated**: November 2025  
**API Version**: 1.0.0
