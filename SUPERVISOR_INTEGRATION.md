# 🎯 Integration Guide for Supervisor Agent

## ✅ Agent Status: RUNNING & READY

Your Sustainability Footprint Agent is now **running and operational** on:
- **Main Endpoint**: `http://localhost:8000/sustainability-footprint-agent`
- **Health Check**: `http://localhost:8000/health`
- **Agent Info**: `http://localhost:8000/`

---

## 📡 API Endpoints for Integration

### 1. Health Check
```
GET http://localhost:8000/health
```

**Response:**
```json
{
  "status": "ok",
  "agent_name": "sustainability-footprint-agent",
  "ready": true
}
```

### 2. Main Agent Endpoint
```
POST http://localhost:8000/sustainability-footprint-agent
```

**Request Format:**
```json
{
  "messages": [
    {
      "role": "user",
      "content": "Your sustainability query here"
    }
  ]
}
```

**Response Format:**
```json
{
  "agent_name": "sustainability-footprint-agent",
  "status": "success",
  "data": {
    "message": "Detailed analysis and recommendations...",
    "metadata": {
      "source": "generated",
      "query": "Original query"
    }
  },
  "error_message": null
}
```

---

## 🔗 Supervisor Integration

### Step 1: Register Agent in Supervisor

Add this to your supervisor's agent registry:

```python
{
    "name": "sustainability-footprint-agent",
    "description": "Environmental impact analysis and sustainability assessment",
    "url": "http://localhost:8000/sustainability-footprint-agent",
    "health_url": "http://localhost:8000/health",
    "intents": [
        "carbon_footprint_analysis",
        "energy_consumption_tracking",
        "waste_management_assessment",
        "sustainability_metrics",
        "environmental_impact_analysis",
        "green_building_assessment",
        "renewable_energy_recommendations"
    ],
    "timeout": 30
}
```

### Step 2: Intent Matching

The supervisor should route queries containing these keywords to this agent:
- carbon, footprint, co2, emissions
- energy, consumption, electricity
- waste, recycling, trash
- sustainability, environmental, green
- solar, renewable, wind
- building, LEED, efficient

### Step 3: Calling the Agent

```python
import requests

def call_sustainability_agent(user_query):
    """Call the sustainability footprint agent"""
    url = "http://localhost:8000/sustainability-footprint-agent"
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": user_query
            }
        ]
    }
    
    try:
        response = requests.post(
            url,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.Timeout:
        return {
            "agent_name": "sustainability-footprint-agent",
            "status": "error",
            "data": None,
            "error_message": "Request timeout"
        }
    
    except Exception as e:
        return {
            "agent_name": "sustainability-footprint-agent",
            "status": "error",
            "data": None,
            "error_message": str(e)
        }

# Example usage
result = call_sustainability_agent("How can I reduce my carbon footprint?")
print(result)
```

---

## 🧪 Testing from Supervisor

### PowerShell Test
```powershell
$body = @{
    messages = @(
        @{
            role = "user"
            content = "What is my carbon footprint from driving 100 miles?"
        }
    )
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/sustainability-footprint-agent" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"
```

### Python Test
```python
import requests

response = requests.post(
    "http://localhost:8000/sustainability-footprint-agent",
    json={
        "messages": [
            {
                "role": "user",
                "content": "How can I reduce energy consumption at home?"
            }
        ]
    }
)

print(response.json())
```

### cURL Test
```bash
curl -X POST http://localhost:8000/sustainability-footprint-agent \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"What are the benefits of solar panels?"}]}'
```

---

## 📋 Example Queries for Testing

1. **Carbon Footprint**:
   - "What is my carbon footprint from driving 100 miles?"
   - "Calculate CO2 emissions for a round-trip flight NYC to London"
   - "How can I reduce my carbon footprint?"

2. **Energy Consumption**:
   - "How can I reduce energy consumption at home?"
   - "What are the benefits of solar panels?"
   - "Recommend energy-efficient appliances"

3. **Waste Management**:
   - "How can I implement better waste management?"
   - "What are best practices for recycling?"
   - "Help me reduce household waste"

4. **Sustainability Metrics**:
   - "How do I track my sustainability progress?"
   - "What are key environmental KPIs?"
   - "Create a sustainability report"

5. **Green Building**:
   - "What is LEED certification?"
   - "How to make my building more sustainable?"
   - "Energy-efficient building design tips"

---

## 🔄 Response Handling

### Success Response
```json
{
  "agent_name": "sustainability-footprint-agent",
  "status": "success",
  "data": {
    "message": "Analysis results...",
    "metadata": {
      "source": "generated" | "ltm_cache",
      "query": "Original query"
    }
  },
  "error_message": null
}
```

### Error Response
```json
{
  "agent_name": "sustainability-footprint-agent",
  "status": "error",
  "data": null,
  "error_message": "Description of error"
}
```

**Supervisor should**:
- Check `status` field ("success" or "error")
- Extract `data.message` for successful responses
- Show `error_message` if status is "error"
- Never assume success without checking status

---

## 🚀 Running the Agent

### Start Agent
```powershell
cd "C:\Users\hp\OneDrive\Desktop\SPM Project"
.\venv\Scripts\python.exe main.py
```

### Keep Running in Background
```powershell
Start-Process powershell -ArgumentList "-NoExit", "-Command", `
    "cd 'C:\Users\hp\OneDrive\Desktop\SPM Project'; .\venv\Scripts\python.exe main.py"
```

### Stop Agent
Press `Ctrl+C` in the terminal running the agent

---

## 📊 Agent Registry Entry

For your SPM Agent Registry spreadsheet:

| Field | Value |
|-------|-------|
| Agents | Sustainability Footprint Agent |
| Intents | `["carbon_footprint_analysis", "energy_consumption_tracking", "waste_management_assessment", "sustainability_metrics", "environmental_impact_analysis", "green_building_assessment", "renewable_energy_recommendations"]` |
| API URL for agent | `http://localhost:8000/sustainability-footprint-agent` |
| API URL for health check | `http://localhost:8000/health` |
| Members Roll No. | 22k-4826, 22i-8799 |
| Members Name | Sajad Ahmed, Saif-ur-Rehman |
| Input | A prompt about sustainability like "What is my carbon footprint from driving 100 miles?" |
| Expected Response | Detailed analysis with actionable recommendations |
| Description | AI-powered sustainability agent for environmental impact analysis |

---

## ⚠️ Important Notes

1. **Agent Must Be Running**: Supervisor can only call the agent when it's running on port 8000

2. **Timeout Handling**: Set timeout to 30 seconds minimum

3. **Error Handling**: Always check the `status` field in response

4. **Format Compliance**: Agent follows exact SPM format specification

5. **No Authentication**: Currently no auth required (add if needed)

---

## 🔍 Health Monitoring

Supervisor should periodically check agent health:

```python
def check_agent_health():
    try:
        response = requests.get(
            "http://localhost:8000/health",
            timeout=5
        )
        return response.status_code == 200
    except:
        return False
```

---

## 📞 Need Help?

- Agent is running on: `http://localhost:8000`
- Test with: `curl http://localhost:8000/health`
- Full docs in: `API_DOCS.md`

**Agent Status**: ✅ **READY FOR INTEGRATION**
