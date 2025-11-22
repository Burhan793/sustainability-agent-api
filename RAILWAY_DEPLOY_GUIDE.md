# 🚀 Deploy to Railway - Step by Step

## Your agent is ready to deploy! Follow these simple steps:

### Step 1: Create a GitHub Account (if you don't have one)
1. Go to https://github.com
2. Sign up for free

### Step 2: Create a New GitHub Repository
1. Go to https://github.com/new
2. Repository name: `sustainability-agent-api`
3. Make it **Public** (required for free Railway deployment)
4. **DO NOT** initialize with README, .gitignore, or license
5. Click "Create repository"

### Step 3: Push Your Code to GitHub
Run these commands in your terminal:

```powershell
# Configure git (replace with your info)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/sustainability-agent-api.git

# Push code to GitHub
git branch -M main
git push -u origin main
```

### Step 4: Deploy on Railway
1. Go to https://railway.app
2. Click **"Start a New Project"**
3. Click **"Deploy from GitHub repo"**
4. Sign in with your GitHub account
5. Select the `sustainability-agent-api` repository
6. Railway will automatically:
   - Detect your Dockerfile
   - Build the container
   - Deploy your agent
   - Give you a public URL

### Step 5: Get Your API URL
1. In Railway dashboard, click on your project
2. Go to **Settings** tab
3. Click **Generate Domain** under "Networking"
4. Your API will be available at: `https://your-app.up.railway.app`

## ✅ Your API Endpoints Will Be:

**Health Check:** 
```
https://your-app.up.railway.app/api/sustainability-footprint-agent/health
```

**Main Endpoint:**
```
https://your-app.up.railway.app/api/sustainability-footprint-agent
```

## 🧪 Test Your Deployed API

```powershell
# Test health endpoint
curl https://your-app.up.railway.app/api/sustainability-footprint-agent/health

# Test main endpoint
curl -X POST "https://your-app.up.railway.app/api/sustainability-footprint-agent" `
  -H "Content-Type: application/json" `
  -d '{\"query\": \"What is carbon footprint?\"}'
```

## 📝 Update SPM Agent Registry

After deployment, update your Excel sheet with:
- **Main URL:** `https://your-app.up.railway.app/api/sustainability-footprint-agent`
- **Health URL:** `https://your-app.up.railway.app/api/sustainability-footprint-agent/health`
- **Members:** 22k-4826, 22i-8799
- **Names:** Sajad Ahmed, Saif-ur-Rehman

## 💡 Railway Free Tier Details
- ✅ $5 free credit per month
- ✅ No credit card required to start
- ✅ Automatic HTTPS
- ✅ Auto-deploy on git push
- ✅ 500MB RAM, 1GB storage
- ✅ Perfect for your agent!

## 🆘 Need Help?
If Railway asks for payment, use **Render** instead (100% free forever):
1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your repository
5. Render detects Dockerfile automatically
6. Click "Create Web Service"

Your agent will be live in 5 minutes! 🎉
