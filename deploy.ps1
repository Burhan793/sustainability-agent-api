# Quick Start - Deploy to Railway

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Sustainability Footprint Agent" -ForegroundColor Green
Write-Host "Railway Deployment Helper" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is initialized
if (-not (Test-Path ".git")) {
    Write-Host "Step 1: Initializing Git repository..." -ForegroundColor Yellow
    git init
    Write-Host "✓ Git initialized" -ForegroundColor Green
} else {
    Write-Host "✓ Git already initialized" -ForegroundColor Green
}

Write-Host ""
Write-Host "Step 2: Adding files to Git..." -ForegroundColor Yellow
git add .
Write-Host "✓ Files added" -ForegroundColor Green

Write-Host ""
Write-Host "Step 3: Creating commit..." -ForegroundColor Yellow
git commit -m "Deploy Sustainability Footprint Agent"
Write-Host "✓ Commit created" -ForegroundColor Green

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Push to GitHub:" -ForegroundColor Yellow
Write-Host "   git remote add origin <your-github-repo-url>"
Write-Host "   git push -u origin main"
Write-Host ""
Write-Host "2. Deploy on Railway:" -ForegroundColor Yellow
Write-Host "   - Go to https://railway.app" -ForegroundColor Blue
Write-Host "   - Sign up with GitHub"
Write-Host "   - Click 'New Project' → 'Deploy from GitHub repo'"
Write-Host "   - Select your repository"
Write-Host "   - Railway will auto-deploy using Dockerfile"
Write-Host ""
Write-Host "3. Get your API URL:" -ForegroundColor Yellow
Write-Host "   https://<your-app>.railway.app/api/sustainability-footprint-agent"
Write-Host ""
Write-Host "4. Test deployment:" -ForegroundColor Yellow
Write-Host "   Invoke-RestMethod -Uri 'https://<your-app>.railway.app/api/sustainability-footprint-agent/health'"
Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Your agent is ready to deploy! 🚀" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Cyan
