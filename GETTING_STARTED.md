# 🎬 Getting Started - Your First Steps

Welcome! This guide will get your Sustainability Footprint Agent running in just a few minutes.

## ⚡ Super Quick Start (3 Commands)

```powershell
# 1. Run setup script
.\setup.ps1

# 2. Start the agent
python main.py

# 3. Test it (in another terminal)
python test_agent.py
```

**That's it!** Your agent is now running! 🎉

---

## 📝 Important Notes About Errors

### ⚠️ Import Errors (Expected Before Setup)

You might see these errors in VS Code:
- ❌ Import "fastapi" could not be resolved
- ❌ Import "pydantic" could not be resolved  
- ❌ Import "openai" could not be resolved
- ❌ Import "uvicorn" could not be resolved

**This is NORMAL!** These will be fixed when you run the setup script.

### ✅ After Running `.\setup.ps1`

All import errors will disappear because:
1. Virtual environment is created
2. All dependencies are installed
3. VS Code detects the packages

---

## 📋 Detailed Step-by-Step

### Step 1: Open PowerShell

```powershell
cd "c:\Users\hp\OneDrive\Desktop\SPM Project"
```

### Step 2: Run Setup

```powershell
.\setup.ps1
```

This will:
- ✅ Check Python installation
- ✅ Create virtual environment
- ✅ Install all dependencies (FastAPI, Pydantic, OpenAI, etc.)
- ✅ Create .env file
- ✅ Set up directories

**Time**: ~2-3 minutes

### Step 3: (Optional) Add OpenAI Key

If you have an OpenAI API key:

```powershell
# Edit .env file
notepad .env

# Add your key:
OPENAI_API_KEY=your-key-here
```

**Note**: Agent works perfectly WITHOUT OpenAI! It has built-in responses.

### Step 4: Start the Agent

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
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 5: Test It

**Open a NEW PowerShell window** and run:

```powershell
# Simple health check
curl http://localhost:8000/health

# Run full test suite
python test_agent.py

# Try interactive examples
python examples.py
```

---

## 🎯 What To Do If Something Goes Wrong

### Problem: "Python not found"

**Solution**: Install Python 3.8 or higher from https://python.org

### Problem: ".\setup.ps1 cannot be loaded"

**Solution**: Enable script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problem: "Port 8000 already in use"

**Solution**: Use a different port:
```powershell
$env:PORT=8001
python main.py
```

### Problem: "Module not found" after setup

**Solution**: Make sure virtual environment is activated:
```powershell
.\venv\Scripts\Activate
python main.py
```

### Problem: "OpenAI API error"

**Solution**: This is fine! Agent works without OpenAI using rule-based responses.

---

## ✅ Verification Checklist

After setup, verify:

- [ ] `python main.py` starts without errors
- [ ] Can access http://localhost:8000/health in browser
- [ ] `python test_agent.py` shows all tests passing
- [ ] Can send queries and get responses

---

## 🚀 What's Next?

### For Development
1. Edit `agents/workers/sustainability_agent.py` to modify agent behavior
2. Run tests after changes: `python test_agent.py`
3. Try examples: `python examples.py`

### For Deployment
1. Read `DEPLOYMENT.md`
2. Choose a platform (Vercel recommended)
3. Deploy and get public URL
4. Add to SPM Agent Registry

### For Understanding
1. Read `README.md` for overview
2. Check `API_DOCS.md` for API details
3. Review `PROJECT_OVERVIEW.md` for architecture

---

## 📚 Key Files to Know

| File | What It Does |
|------|-------------|
| `main.py` | Starts the agent |
| `api.py` | Defines API endpoints |
| `agents/workers/sustainability_agent.py` | Main agent logic |
| `test_agent.py` | Tests everything |
| `examples.py` | Shows how to use the agent |

---

## 💡 Pro Tips

### Tip 1: Keep Agent Running
Leave `python main.py` running in one terminal window while you test in another.

### Tip 2: Check Logs
Watch the terminal where the agent is running to see requests coming in.

### Tip 3: Use Examples
Run `python examples.py` to see different ways to query the agent.

### Tip 4: Test Often
After any code change, run `python test_agent.py` to make sure nothing broke.

### Tip 5: Read Error Messages
The agent returns helpful error messages. Read them to understand what went wrong.

---

## 🎓 Understanding Your Agent

### How It Works

1. **User sends query** → Your API endpoint
2. **Agent checks cache** → LTM (Long-Term Memory)
3. **If not cached** → Generate new response
4. **Use OpenAI** (if available) or rule-based system
5. **Store in cache** → For next time
6. **Return response** → Standard format

### Key Components

- **FastAPI**: Web server and API framework
- **Pydantic**: Data validation (ensures correct format)
- **OpenAI**: Advanced AI (optional)
- **LTM**: Caching for performance
- **Rule-based**: Always-working fallback

---

## 📞 Need Help?

### Check Documentation
1. `QUICKSTART.md` - Fast setup
2. `README.md` - Complete guide
3. `API_DOCS.md` - API reference
4. `DEPLOYMENT.md` - How to deploy

### Common Questions

**Q: Do I need OpenAI API key?**  
A: No! Agent works great without it.

**Q: How do I deploy this?**  
A: See `DEPLOYMENT.md` - Vercel is easiest.

**Q: Can I modify the agent?**  
A: Yes! Edit `agents/workers/sustainability_agent.py`

**Q: How do I add new intents?**  
A: Update `communication/protocol.py` and `config/agent_config.json`

**Q: Tests are failing?**  
A: Make sure agent is running: `python main.py`

---

## 🎉 Success!

If you can:
1. ✅ Run `python main.py` without errors
2. ✅ Access http://localhost:8000/health
3. ✅ See all tests pass in `python test_agent.py`

**You're ready to go!** 🚀

---

## 🎯 Your Mission

1. **Get it running locally** ✅
2. **Understand how it works** 📚
3. **Deploy to production** 🚀
4. **Register with supervisor** 📝
5. **Demo to your team** 🎬

---

**You've got this!** The agent is production-ready and all the documentation is here to help you succeed. 💪

**Start now**: Run `.\setup.ps1` and watch the magic happen! ✨

---

**Quick Reference Card**

```powershell
# Start Agent
python main.py

# Run Tests  
python test_agent.py

# Try Examples
python examples.py

# Health Check
curl http://localhost:8000/health

# Stop Agent
Ctrl+C
```

---

**Ready? Let's go!** 🚀
