# 🚀 Quick Deployment Guide

## Deploy Your Agent to the Cloud (PC-Independent)

Your Sustainability Footprint Agent can now run 24/7 on cloud platforms. Choose one option below:

---

## Option 1: Railway (Recommended - Easiest)

### Steps:
1. **Sign up**: Go to [railway.app](https://railway.app) and sign up with GitHub
2. **New Project**: Click "New Project" → "Deploy from GitHub repo"
3. **Connect Repository**: 
   - Push your code to GitHub first (or use Railway CLI)
   - Select your repository
4. **Auto-Deploy**: Railway will detect `railway.json` and `Dockerfile` automatically
5. **Get URL**: Railway provides a URL like `https://your-app.railway.app`

### Your API Endpoints:
```
https://your-app.railway.app/api/sustainability-footprint-agent
https://your-app.railway.app/api/sustainability-footprint-agent/health
```

### Environment Variables (Optional):
- `OPENAI_API_KEY`: Your OpenAI key (if you want AI responses instead of rule-based)

**Cost**: Free tier includes $5/month credit (enough for development)

---

## Option 2: Render

### Steps:
1. **Sign up**: Go to [render.com](https://render.com) and create account
2. **New Web Service**: Click "New +" → "Web Service"
3. **Connect GitHub**: Link your repository
4. **Auto-Detect**: Render will use `render.yaml` configuration
5. **Deploy**: Click "Create Web Service"
6. **Get URL**: Render provides `https://your-app.onrender.com`

### Your API Endpoints:
```
https://your-app.onrender.com/api/sustainability-footprint-agent
https://your-app.onrender.com/api/sustainability-footprint-agent/health
```

**Cost**: Free tier available (spins down after inactivity, cold start ~30s)

---

## Option 3: Fly.io

### Steps:
1. **Install Fly CLI**: 
   ```powershell
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   ```

2. **Login**:
   ```powershell
   fly auth login
   ```

3. **Launch App**:
   ```powershell
   fly launch
   ```

4. **Deploy**:
   ```powershell
   fly deploy
   ```

5. **Get URL**: Fly provides `https://your-app.fly.dev`

### Your API Endpoints:
```
https://your-app.fly.dev/api/sustainability-footprint-agent
https://your-app.fly.dev/api/sustainability-footprint-agent/health
```

**Cost**: Free tier includes 3 shared VMs

---

## Option 4: Vercel (Serverless)

### Steps:
1. **Install Vercel CLI**:
   ```powershell
   npm install -g vercel
   ```

2. **Deploy**:
   ```powershell
   vercel
   ```

3. **Follow prompts** to link project
4. **Get URL**: Vercel provides `https://your-app.vercel.app`

**Note**: Vercel is serverless, so cold starts are expected

---

## Pre-Deployment Checklist

Before deploying, ensure:

- [ ] Code pushed to GitHub (recommended) or use CLI
- [ ] `requirements.txt` is up to date
- [ ] `.env` file is NOT in repository (use platform environment variables)
- [ ] Test locally first: `python main.py`

---

## After Deployment

### 1. Test Your Live API

```powershell
# Health check
Invoke-RestMethod -Uri "https://your-deployed-url/api/sustainability-footprint-agent/health"

# Test query
$body = @{
    messages = @(
        @{
            role = "user"
            content = "What is carbon footprint?"
        }
    )
} | ConvertTo-Json -Depth 3

Invoke-RestMethod -Uri "https://your-deployed-url/api/sustainability-footprint-agent" `
    -Method POST `
    -Body $body `
    -ContentType "application/json"
```

### 2. Update SPM Agent Registry

Replace `<ip>` with your deployed URL:
```
https://your-app.railway.app/api/sustainability-footprint-agent
https://your-app.railway.app/api/sustainability-footprint-agent/health
```

### 3. Share with Supervisor Team

Provide them with:
- **Main Endpoint**: `https://your-app.railway.app/api/sustainability-footprint-agent`
- **Health Endpoint**: `https://your-app.railway.app/api/sustainability-footprint-agent/health`
- **Agent Name**: `sustainability-footprint-agent`
- **Intents**: carbon_footprint_analysis, energy_consumption_tracking, etc.

---

## Troubleshooting

### Deployment fails?
- Check logs on platform dashboard
- Ensure Python version is 3.13+ (specified in Dockerfile)
- Verify all dependencies in `requirements.txt`

### API returns 500 error?
- Check platform logs
- Ensure environment variables are set (if using OpenAI)
- Verify health endpoint works first

### Slow responses?
- Free tiers may have cold starts (first request after inactivity)
- Consider paid tier for always-on instances
- Railway and Fly.io have better free tier performance

---

## Cost Comparison

| Platform | Free Tier | Always-On | Cold Start |
|----------|-----------|-----------|------------|
| Railway  | $5/month credit | Yes | No |
| Render   | 750 hours/month | No | Yes (~30s) |
| Fly.io   | 3 VMs | Yes | No |
| Vercel   | Unlimited | No | Yes (~1-5s) |

**Recommendation**: Use **Railway** for best free tier experience with no cold starts.

---

## Local Testing (Before Deploy)

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Start agent
python main.py

# Test in another terminal
Invoke-RestMethod -Uri "http://localhost:8000/api/sustainability-footprint-agent/health"
```

---

## Next Steps

1. Choose a platform (Railway recommended)
2. Deploy your agent
3. Test the live API
4. Update SPM Agent Registry with your URL
5. Share API endpoint with supervisor team

Your agent will now run 24/7 independent of your PC! 🎉
