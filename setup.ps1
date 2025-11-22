# Setup Script for Sustainability Footprint Agent
# Run this script to set up the project

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Sustainability Footprint Agent - Setup Script" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "[1/6] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  ✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Python not found! Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host ""
Write-Host "[2/6] Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "  ℹ Virtual environment already exists" -ForegroundColor Blue
} else {
    python -m venv venv
    Write-Host "  ✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host ""
Write-Host "[3/6] Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
Write-Host "  ✓ Virtual environment activated" -ForegroundColor Green

# Install dependencies
Write-Host ""
Write-Host "[4/6] Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt --quiet
Write-Host "  ✓ Dependencies installed" -ForegroundColor Green

# Create .env file if it doesn't exist
Write-Host ""
Write-Host "[5/6] Setting up environment variables..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "  ℹ .env file already exists" -ForegroundColor Blue
} else {
    Copy-Item ".env.example" ".env"
    Write-Host "  ✓ .env file created from template" -ForegroundColor Green
    Write-Host "  ℹ Please edit .env and add your OPENAI_API_KEY (optional)" -ForegroundColor Blue
}

# Create logs directory
Write-Host ""
Write-Host "[6/6] Creating directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "logs" | Out-Null
New-Item -ItemType Directory -Force -Path "shared\LTM\sustainability-footprint-agent" | Out-Null
Write-Host "  ✓ Directories created" -ForegroundColor Green

# Summary
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Setup Complete! ✓" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. (Optional) Edit .env file to add your OpenAI API key" -ForegroundColor White
Write-Host "  2. Run the agent:  python main.py" -ForegroundColor White
Write-Host "  3. Run tests:      python test_agent.py" -ForegroundColor White
Write-Host "  4. View examples:  python examples.py" -ForegroundColor White
Write-Host ""
Write-Host "Documentation:" -ForegroundColor Yellow
Write-Host "  • Quick Start:     QUICKSTART.md" -ForegroundColor White
Write-Host "  • Full README:     README.md" -ForegroundColor White
Write-Host "  • API Docs:        API_DOCS.md" -ForegroundColor White
Write-Host "  • Deployment:      DEPLOYMENT.md" -ForegroundColor White
Write-Host ""
Write-Host "Ready to start? Run:  python main.py" -ForegroundColor Green
Write-Host ""
