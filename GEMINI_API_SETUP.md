# 🚀 Get Your FREE Google Gemini API Key

## Why Gemini?
- ✅ **100% FREE** - No credit card required
- ✅ **Unlimited requests** - High rate limits (15 requests/min, 1500/day)
- ✅ **Better than GPT-3.5** - More accurate and faster
- ✅ **Better than Groq** - More reliable, no rate limit issues
- ✅ **Latest AI** - Gemini 1.5 Flash model

---

## 📝 Step-by-Step Instructions

### Step 1: Go to Google AI Studio
Open this link: **https://aistudio.google.com/app/apikey**

### Step 2: Sign in with Google
- Use any Gmail account (your personal account works fine)
- Click "Get API Key"

### Step 3: Create API Key
1. Click **"Create API key"** button
2. Select **"Create API key in new project"**
3. Your API key will appear - **COPY IT** (looks like: `AIzaSyXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx`)

### Step 4: Add to Railway
1. Go to **https://railway.app** → Your project
2. Click on your **sustainability-agent-api** service
3. Go to **"Variables"** tab
4. Click **"+ New Variable"**
5. Add:
   - **Variable Name:** `GEMINI_API_KEY`
   - **Value:** Paste your API key here
6. Click **"Add"**

### Step 5: Redeploy
Railway will automatically redeploy with the new API key.

**Wait 1-2 minutes**, then test your agent!

---

## 🧪 Test After Setup

```powershell
# Test with a query
$body = @{
    messages = @(
        @{
            role = "user"
            content = "What is carbon footprint?"
        }
    )
} | ConvertTo-Json -Depth 10

Invoke-RestMethod -Uri "https://web-production-4c3336.up.railway.app/api/sustainability-footprint-agent" -Method Post -ContentType "application/json" -Body $body
```

You should now get **unique AI-generated responses** for every query! 🎉

---

## 📊 What Changes:

### Before (Rule-based):
```
Query 1: "What is carbon footprint?"
Response: Carbon footprint analysis involves measuring total greenhouse gas emissions...

Query 2: "What is carbon footprint?"  
Response: Carbon footprint analysis involves measuring total greenhouse gas emissions...
(Same response)
```

### After (Gemini AI):
```
Query 1: "What is carbon footprint?"
Response: A carbon footprint is the total amount of greenhouse gases produced directly and indirectly by an individual, organization, or product. It's typically measured in tons of CO2 equivalent...

Query 2: "What is carbon footprint?"
Response: Your carbon footprint represents the cumulative environmental impact of your activities through greenhouse gas emissions. This includes transportation, energy use, food choices, and consumption patterns...
(Different, unique response!)
```

---

## ⚠️ Important Notes:

1. **Keep API Key Secret** - Don't share it publicly
2. **Free Tier Limits:**
   - 15 requests per minute
   - 1,500 requests per day
   - 1 million tokens per day
3. **Completely FREE** - No credit card ever needed
4. **Works Forever** - Free tier doesn't expire

---

## 🎯 Quick Summary:

1. Visit: https://aistudio.google.com/app/apikey
2. Create API key (1 click)
3. Add to Railway Variables as `GEMINI_API_KEY`
4. Done! Your agent now uses AI! 🚀

**Questions?** The API key is a simple copy-paste process that takes 2 minutes!
