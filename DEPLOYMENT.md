# Deployment Guide - Sustainability Footprint Agent

This guide covers deploying your Sustainability Footprint Agent to various platforms.

## 📋 Pre-Deployment Checklist

- [ ] All tests pass (`python test_agent.py`)
- [ ] Dependencies are up to date (`requirements.txt`)
- [ ] Configuration files are properly set
- [ ] Environment variables are configured
- [ ] Agent responds correctly to all intents
- [ ] Health check endpoint works

## 🚀 Deployment Options

### Option 1: Vercel (Recommended for Quick Deployment)

**Pros**: Free tier, automatic HTTPS, easy deployment  
**Cons**: Serverless (some limitations on long-running processes)

#### Steps:

1. **Install Vercel CLI**:
```powershell
npm install -g vercel
```

2. **Create `vercel.json`**:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api.py"
    }
  ],
  "env": {
    "OPENAI_API_KEY": "@openai-api-key"
  }
}
```

3. **Add environment variable**:
```powershell
vercel env add OPENAI_API_KEY
```

4. **Deploy**:
```powershell
vercel --prod
```

5. **Get your URL** and update the SPM Agent Registry.

---

### Option 2: Hugging Face Spaces

**Pros**: Free GPU options, ML-focused, easy sharing  
**Cons**: Requires specific structure

#### Steps:

1. **Create a new Space** on [Hugging Face](https://huggingface.co/spaces)
2. **Select** "Gradio" or "Docker" SDK
3. **Create `app.py`** wrapper:
```python
import gradio as gr
from api import app
import uvicorn
from threading import Thread

def run_server():
    uvicorn.run(app, host="0.0.0.0", port=7860)

Thread(target=run_server, daemon=True).start()

# Gradio interface for documentation
iface = gr.Interface(
    fn=lambda x: "Agent running at /sustainability-footprint-agent",
    inputs="text",
    outputs="text",
    title="Sustainability Footprint Agent"
)

iface.launch(server_port=7860)
```

4. **Push your code** to the Space repository
5. **Add secrets** in Space settings

---

### Option 3: Render

**Pros**: Free tier, persistent storage, easy setup  
**Cons**: May sleep after inactivity on free tier

#### Steps:

1. **Create account** at [Render.com](https://render.com)
2. **Create new Web Service**
3. **Connect GitHub repository** or deploy manually
4. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Port**: 8000

5. **Add environment variables** in Render dashboard
6. **Deploy**

---

### Option 4: Railway

**Pros**: Simple deployment, good free tier  
**Cons**: Credit-based billing

#### Steps:

1. **Install Railway CLI**:
```powershell
npm i -g @railway/cli
```

2. **Initialize**:
```powershell
railway login
railway init
```

3. **Deploy**:
```powershell
railway up
```

4. **Add environment variables**:
```powershell
railway variables set OPENAI_API_KEY=your-key
```

---

### Option 5: Docker (Any Platform)

**Pros**: Platform-agnostic, consistent environment  
**Cons**: Requires Docker knowledge

#### Steps:

1. **Create `Dockerfile`**:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

2. **Create `.dockerignore`**:
```
__pycache__
*.pyc
venv/
.env
.git/
```

3. **Build image**:
```powershell
docker build -t sustainability-agent .
```

4. **Run container**:
```powershell
docker run -p 8000:8000 -e OPENAI_API_KEY=your-key sustainability-agent
```

5. **Deploy to**:
   - Docker Hub
   - Google Cloud Run
   - AWS ECS
   - Azure Container Instances

---

### Option 6: PythonAnywhere

**Pros**: Python-specific, free tier available  
**Cons**: Limited resources on free tier

#### Steps:

1. **Create account** at [PythonAnywhere](https://www.pythonanywhere.com)
2. **Upload files** via web interface or git
3. **Install dependencies** in bash console:
```bash
pip install --user -r requirements.txt
```

4. **Create WSGI file**:
```python
import sys
sys.path.append('/home/yourusername/sustainability-agent')

from api import app as application
```

5. **Configure web app** in PythonAnywhere dashboard
6. **Reload** the web app

---

## 🔧 Post-Deployment Configuration

### 1. Update Agent Registry

Add your deployed agent to the SPM Agent Registry sheet:

```json
{
  "name": "sustainability-footprint-agent",
  "description": "Environmental impact analysis and sustainability assessment",
  "url": "https://your-deployment-url.com/sustainability-footprint-agent",
  "health_url": "https://your-deployment-url.com/health",
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

### 2. Test Deployed Agent

```powershell
# Health check
curl https://your-deployment-url.com/health

# Test query
curl -X POST https://your-deployment-url.com/sustainability-footprint-agent `
  -H "Content-Type: application/json" `
  -d '{\"messages\": [{\"role\": \"user\", \"content\": \"Test query\"}]}'
```

### 3. Monitor Performance

- Check response times
- Monitor error rates
- Track LTM cache hit rates
- Verify health check endpoint

### 4. Set Up Logging (Optional)

For production, consider:
- Sentry for error tracking
- LogRocket for session replay
- CloudWatch/Stackdriver for logs

---

## 🔒 Security Best Practices

1. **Never commit API keys** - Use environment variables
2. **Enable CORS properly** - Restrict origins in production
3. **Add rate limiting** - Prevent abuse
4. **Use HTTPS** - Most platforms provide this automatically
5. **Validate inputs** - Already implemented in Pydantic models
6. **Monitor usage** - Track API calls and costs

---

## 📊 Monitoring & Maintenance

### Health Checks

Set up automated health checks:
```powershell
# Using cron or task scheduler
curl -f https://your-url.com/health || echo "Agent down!"
```

### Performance Monitoring

Track these metrics:
- Response time (should be < 30s)
- Error rate (should be < 1%)
- Cache hit rate (LTM effectiveness)
- Memory usage
- API costs (if using OpenAI)

### Logs

Check logs regularly for:
- Error patterns
- Unusual queries
- Performance bottlenecks
- Cache efficiency

---

## 🆘 Troubleshooting

### Agent Not Responding
1. Check health endpoint
2. Verify environment variables
3. Check logs for errors
4. Ensure dependencies installed

### Slow Response Times
1. Check OpenAI API status
2. Verify network connectivity
3. Consider caching frequently asked queries
4. Optimize LTM lookups

### Memory Issues
1. Clean up LTM cache periodically
2. Limit cache size in config
3. Upgrade to larger instance

### Integration Issues
1. Verify request/response format
2. Check CORS settings
3. Validate agent registry entry
4. Test with curl/Postman first

---

## 📈 Scaling Considerations

For high traffic:
1. **Use load balancer** - Distribute requests
2. **Horizontal scaling** - Multiple instances
3. **Redis for LTM** - Shared cache across instances
4. **CDN for static content** - Faster responses
5. **Rate limiting** - Protect against abuse

---

## ✅ Deployment Checklist

Before going live:

- [ ] All endpoints tested
- [ ] Health check working
- [ ] Error handling verified
- [ ] Environment variables set
- [ ] CORS configured
- [ ] Rate limiting implemented (optional)
- [ ] Logging configured
- [ ] Monitoring set up
- [ ] Agent registered in SPM registry
- [ ] Documentation updated with deployment URL
- [ ] Team members can access
- [ ] Backup plan in place

---

## 🎯 Recommended: Vercel Deployment

For this project, **Vercel** is recommended because:
- ✅ Free and fast
- ✅ Automatic HTTPS
- ✅ Simple deployment
- ✅ Good for demos
- ✅ Easy rollback

Quick deploy:
```powershell
npm i -g vercel
vercel --prod
```

Done! 🚀
