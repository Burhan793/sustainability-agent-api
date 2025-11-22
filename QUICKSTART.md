# Quick Start Guide - Sustainability Footprint Agent

Get your agent up and running in 5 minutes! 🚀

## Step 1: Installation (2 minutes)

### Open PowerShell in your project directory:
```powershell
cd "c:\Users\hp\OneDrive\Desktop\SPM Project"
```

### Create and activate virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

### Install dependencies:
```powershell
pip install -r requirements.txt
```

## Step 2: Configuration (1 minute)

### (Optional) Add OpenAI API Key:

If you have an OpenAI API key for enhanced responses:

```powershell
# Create .env file
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

**Without OpenAI key**: The agent still works using built-in rule-based responses!

## Step 3: Run the Agent (30 seconds)

```powershell
python main.py
```

You should see:
```
============================================================
Sustainability Footprint Agent
============================================================
Host: 0.0.0.0
Port: 8000
Health Check: http://localhost:8000/health
Main Endpoint: http://localhost:8000/sustainability-footprint-agent
============================================================
```

## Step 4: Test the Agent (1.5 minutes)

### Test 1: Health Check
Open a new PowerShell window:
```powershell
curl http://localhost:8000/health
```

Expected output:
```json
{
  "status": "ok",
  "agent_name": "sustainability-footprint-agent",
  "ready": true
}
```

### Test 2: Send a Query
```powershell
curl -X POST http://localhost:8000/sustainability-footprint-agent `
  -H "Content-Type: application/json" `
  -d '{\"messages\": [{\"role\": \"user\", \"content\": \"How can I reduce my carbon footprint?\"}]}'
```

### Test 3: Run Full Test Suite
```powershell
python test_agent.py
```

### Test 4: Try Examples
```powershell
python examples.py
```

## Step 5: What's Next?

### For Development:
1. Modify agent behavior in `agents/workers/sustainability_agent.py`
2. Update intents in `communication/protocol.py`
3. Adjust configuration in `config/settings.yaml`

### For Deployment:
1. See `DEPLOYMENT.md` for deployment options
2. Vercel is recommended for quick deployment
3. Update SPM Agent Registry with your deployed URL

### For Integration:
Add to SPM Agent Registry sheet:
```json
{
  "name": "sustainability-footprint-agent",
  "url": "http://your-ip:8000/sustainability-footprint-agent",
  "health_url": "http://your-ip:8000/health",
  "intents": ["carbon_footprint_analysis", "energy_consumption_tracking", ...]
}
```

## Common Issues & Solutions

### Issue: "Module not found"
**Solution**: Make sure virtual environment is activated and dependencies installed:
```powershell
.\venv\Scripts\Activate
pip install -r requirements.txt
```

### Issue: "Port already in use"
**Solution**: Change port in `config/settings.yaml` or use environment variable:
```powershell
$env:PORT=8001
python main.py
```

### Issue: "OpenAI API error"
**Solution**: The agent works without OpenAI! It uses rule-based responses as fallback.

## Quick Reference

| Action | Command |
|--------|---------|
| Start agent | `python main.py` |
| Run tests | `python test_agent.py` |
| View examples | `python examples.py` |
| Health check | `curl http://localhost:8000/health` |
| Stop agent | `Ctrl+C` |

## Example Queries to Try

1. "Calculate the carbon footprint of a 1000 mile road trip"
2. "What are the benefits of solar panels?"
3. "How can I reduce waste in my office?"
4. "What is the environmental impact of air travel?"
5. "Recommend energy-efficient appliances"

## Need Help?

- 📖 Full documentation: `README.md`
- 🚀 Deployment guide: `DEPLOYMENT.md`
- 🧪 Test script: `test_agent.py`
- 💡 Usage examples: `examples.py`

---

**You're all set! The agent is ready to analyze sustainability footprints! 🌍**
