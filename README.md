# Sustainability Footprint Agent

A specialized AI agent for environmental impact analysis, carbon footprint calculations, and sustainability assessment as part of a Multi-Agent System.

## 🚀 Quick Deploy

**Your agent is ready to deploy to the cloud!** See [CLOUD_DEPLOYMENT.md](CLOUD_DEPLOYMENT.md) for step-by-step instructions.

**API Endpoints:**
- Local: `http://localhost:8000/api/sustainability-footprint-agent`
- Production: `https://<your-domain>/api/sustainability-footprint-agent`

## 🌍 Overview

The Sustainability Footprint Agent provides intelligent analysis and recommendations for:
- **Carbon Footprint Analysis**: Calculate and reduce CO2 emissions
- **Energy Consumption Tracking**: Monitor and optimize energy usage
- **Waste Management Assessment**: Evaluate recycling and waste reduction
- **Renewable Energy Recommendations**: Solar, wind, and other green solutions
- **Green Building Assessment**: Sustainability certifications and standards
- **Environmental Impact Analysis**: Comprehensive sustainability metrics

## 📁 Project Structure

```
/multi-agent-system
├── /agents                    # All executable agent code
│   ├── /supervisor           # Supervisor-specific logic
│   ├── /workers              # Worker-specific implementations
│   │   └── sustainability_agent.py
│   └── worker_base.py        # AbstractWorkerAgent class
├── /communication            # Shared message schemas and protocols
│   ├── models.py            # Pydantic models for requests/responses
│   └── protocol.py          # Enum/constants for message types
├── /config                   # System and agent configuration
│   ├── settings.yaml        # Global settings
│   └── agent_config.json    # Agent-specific configurations
├── /shared                   # Reusable utilities and resources
│   ├── /LTM                 # Long-term memory storage
│   ├── utils.py             # Helper functions
│   └── ltm_storage.py       # LTM implementation
├── api.py                    # FastAPI application
├── main.py                   # System entry point
└── requirements.txt          # Project dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or navigate to the project directory**:
```powershell
cd "c:\Users\hp\OneDrive\Desktop\SPM Project"
```

2. **Create a virtual environment** (recommended):
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

3. **Install dependencies**:
```powershell
pip install -r requirements.txt
```

4. **(Optional) Set up OpenAI API key** for enhanced AI responses:
```powershell
# Create a .env file
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

### Running the Agent

**Option 1: Using main.py** (Recommended)
```powershell
python main.py
```

**Option 2: Using api.py directly**
```powershell
python api.py
```

**Option 3: Using uvicorn**
```powershell
uvicorn api:app --host 0.0.0.0 --port 8000
```

The agent will start on `http://localhost:8000`

## 📡 API Endpoints

### 1. Health Check
```
GET /api/sustainability-footprint-agent/health
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
POST /api/sustainability-footprint-agent
```

**Request Format:**
```json
{
  "messages": [
    {
      "role": "user",
      "content": "What is my carbon footprint from driving 100 miles?"
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
    "message": "Your analysis results...",
    "metadata": {
      "source": "generated",
      "query": "What is my carbon footprint..."
    }
  },
  "error_message": null
}
```

### 3. Agent Information
```
GET /
```

Returns agent metadata including intents and capabilities.

## 🧪 Testing the Agent

### Using cURL
```powershell
# Health check
curl http://localhost:8000/api/sustainability-footprint-agent/health

# Send a query
curl -X POST http://localhost:8000/api/sustainability-footprint-agent `
  -H "Content-Type: application/json" `
  -d '{\"messages\": [{\"role\": \"user\", \"content\": \"How can I reduce my carbon footprint?\"}]}'
```

### Using Python
```python
import requests

# Health check
response = requests.get("http://localhost:8000/api/sustainability-footprint-agent/health")
print(response.json())

# Send a query
response = requests.post(
    "http://localhost:8000/api/sustainability-footprint-agent",
    json={
        "messages": [
            {"role": "user", "content": "What are the benefits of solar panels?"}
        ]
    }
)
print(response.json())
```

## 🎯 Supported Intents

The agent handles the following sustainability-related queries:
- `carbon_footprint_analysis`
- `energy_consumption_tracking`
- `waste_management_assessment`
- `sustainability_metrics`
- `environmental_impact_analysis`
- `green_building_assessment`
- `renewable_energy_recommendations`

## 🧠 Long-Term Memory (LTM)

The agent implements intelligent caching:
- Stores successful responses for faster retrieval
- Uses query hashing for efficient lookup
- Tracks access counts and timestamps
- Automatically manages cache storage

LTM files are stored in: `shared/LTM/sustainability-footprint-agent/`

## ⚙️ Configuration

### settings.yaml
Global system configuration including API settings, timeouts, and LTM configuration.

### agent_config.json
Agent-specific configuration including:
- Agent name and description
- API endpoints (main and health)
- Supported intents
- Capabilities and version

## 🔌 Integration with Supervisor

The agent is designed to work within a multi-agent system:

1. **Registry Entry** (for supervisor):
```json
{
  "name": "sustainability-footprint-agent",
  "url": "http://your-ip:8000/sustainability-footprint-agent",
  "health_url": "http://your-ip:8000/health",
  "intents": ["carbon_footprint_analysis", "energy_consumption_tracking", ...]
}
```

2. Add this to the SPM-Agent-Registry sheet for supervisor discovery.

## 🌐 Deployment

### Local Development
```powershell
python main.py
```

### Production Deployment Options

**Vercel** (Recommended for quick deployment):
1. Install Vercel CLI: `npm i -g vercel`
2. Create `vercel.json`:
```json
{
  "builds": [{"src": "api.py", "use": "@vercel/python"}],
  "routes": [{"src": "/(.*)", "dest": "api.py"}]
}
```
3. Deploy: `vercel --prod`

**Hugging Face Spaces**:
1. Create a new Space with Gradio SDK
2. Push your code
3. The app will auto-deploy

**Docker**:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## 🛡️ Error Handling

The agent implements robust error handling:
- Always returns valid JSON responses
- Never crashes on invalid input
- Includes timeout protection
- Provides meaningful error messages
- Status is always "success" or "error"

## 📝 Example Queries

- "What is my carbon footprint from daily commuting?"
- "How much energy do solar panels save?"
- "What are best practices for waste reduction?"
- "Calculate CO2 emissions for a 500-mile flight"
- "Recommend green building certifications"
- "How can I make my home more energy efficient?"

## 🤝 Contributing

This agent is part of the SPM Multi-Agent System project. For modifications:
1. Update agent logic in `agents/workers/sustainability_agent.py`
2. Modify API endpoints in `api.py`
3. Update configurations in `config/` directory
4. Test thoroughly before deployment

## 📄 License

Part of the SPM Project Multi-Agent System.

## 📞 Support

For issues or questions about this agent, contact your SPM project team.

---

**Agent Version**: 1.0.0  
**Last Updated**: November 2025
