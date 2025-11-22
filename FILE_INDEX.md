# 📁 Project File Index

Complete reference of all files in the Sustainability Footprint Agent project.

## 📂 Directory Structure

```
SPM Project/
├── agents/                              # Agent implementations
│   ├── __init__.py                      # Package initialization
│   ├── worker_base.py                   # Abstract base class for workers
│   ├── workers/                         # Worker agent implementations
│   │   ├── __init__.py                  # Package initialization
│   │   └── sustainability_agent.py      # Main agent implementation
│   └── supervisor/                      # Supervisor agent (placeholder)
│       └── __init__.py                  # Package initialization
│
├── communication/                       # Communication protocols & models
│   ├── __init__.py                      # Package exports
│   ├── models.py                        # Pydantic models (Request/Response)
│   └── protocol.py                      # Message types & intents
│
├── config/                              # Configuration files
│   ├── settings.yaml                    # Global system settings
│   └── agent_config.json                # Agent metadata & registry info
│
├── shared/                              # Shared utilities & resources
│   ├── __init__.py                      # Package exports
│   ├── utils.py                         # Helper functions & ConfigLoader
│   ├── ltm_storage.py                   # Long-Term Memory implementation
│   └── LTM/                             # LTM storage directory
│       └── sustainability-footprint-agent/  # Agent-specific cache
│           └── memory.json              # (Created at runtime)
│
├── api.py                               # FastAPI application
├── main.py                              # System entry point
├── requirements.txt                     # Python dependencies
│
├── test_agent.py                        # Comprehensive test suite
├── examples.py                          # Usage examples
├── postman_collection.json              # Postman API tests
│
├── .env.example                         # Environment variable template
├── .gitignore                           # Git ignore rules
├── setup.ps1                            # Automated setup script
│
├── README.md                            # Main project documentation
├── QUICKSTART.md                        # 5-minute quick start guide
├── API_DOCS.md                          # Complete API documentation
├── DEPLOYMENT.md                        # Deployment guide
├── PROJECT_OVERVIEW.md                  # Project architecture & overview
├── CHECKLIST.md                         # Pre-deployment checklist
└── FILE_INDEX.md                        # This file
```

---

## 📄 File Descriptions

### Core Implementation Files

#### `agents/worker_base.py`
**Purpose**: Abstract base class for all worker agents  
**Key Components**:
- `AbstractWorkerAgent` class
- Abstract methods: `process_task()`, `send_message()`, `write_to_ltm()`, `read_from_ltm()`
- Concrete methods: `handle_incoming_message()`, `_execute_task()`, `_report_completion()`

**When to Edit**: When changing base worker behavior or protocol

#### `agents/workers/sustainability_agent.py`
**Purpose**: Main sustainability agent implementation  
**Key Components**:
- `SustainabilityFootprintAgent` class
- Business logic for sustainability analysis
- OpenAI integration (optional)
- Rule-based fallback responses
- LTM integration
- API request processing

**When to Edit**: To modify agent behavior, add new analysis types, or update responses

#### `api.py`
**Purpose**: FastAPI web server and endpoints  
**Key Components**:
- FastAPI app initialization
- POST /sustainability-footprint-agent endpoint
- GET /health endpoint
- GET / (info) endpoint
- CORS middleware
- Error handlers
- Timeout middleware

**When to Edit**: To add new endpoints or modify API behavior

#### `main.py`
**Purpose**: Application entry point  
**Key Components**:
- Configuration loading
- Server initialization
- Logging setup

**When to Edit**: To change startup behavior or configuration loading

---

### Communication & Data Models

#### `communication/models.py`
**Purpose**: Pydantic data models for API  
**Key Components**:
- `Status` enum (success/error)
- `Role` enum (user/assistant/system)
- `Message` model
- `AgentRequest` model
- `AgentResponse` model
- `HealthCheckResponse` model

**When to Edit**: When API format changes or new models needed

#### `communication/protocol.py`
**Purpose**: Communication protocol definitions  
**Key Components**:
- `MessageType` enum
- `TaskPriority` enum
- `AgentStatus` enum
- `SUSTAINABILITY_INTENTS` list

**When to Edit**: To add new intents or message types

---

### Configuration Files

#### `config/settings.yaml`
**Purpose**: Global system configuration  
**Key Components**:
- System settings
- Supervisor configuration
- Worker settings
- API configuration
- OpenAI settings
- LTM configuration
- Logging configuration

**When to Edit**: To change system-wide settings

#### `config/agent_config.json`
**Purpose**: Agent metadata for registry  
**Key Components**:
- Agent name and description
- URL endpoints
- Intents list
- Capabilities
- Version info

**When to Edit**: When deploying or changing agent capabilities

---

### Shared Utilities

#### `shared/utils.py`
**Purpose**: Shared helper functions  
**Key Components**:
- `setup_logging()` - Configure logging
- `load_yaml_config()` - Load YAML files
- `load_json_config()` - Load JSON files
- `get_timestamp()` - ISO timestamp
- `ConfigLoader` class

**When to Edit**: To add new utility functions

#### `shared/ltm_storage.py`
**Purpose**: Long-Term Memory implementation  
**Key Components**:
- `LTMStorage` class
- `write()` - Store key-value pairs
- `read()` - Retrieve values
- `search_similar()` - Find cached responses
- `store_response()` - Cache query results

**When to Edit**: To modify caching behavior

---

### Testing & Examples

#### `test_agent.py`
**Purpose**: Automated test suite  
**Tests**:
- ✓ Health check
- ✓ Agent info
- ✓ Carbon footprint queries
- ✓ Energy queries
- ✓ Waste management queries
- ✓ LTM caching
- ✓ Error handling

**When to Run**: Before deployment, after changes

#### `examples.py`
**Purpose**: Usage examples and demonstrations  
**Examples**:
- Basic queries
- Multi-turn conversations
- Specific calculations
- Recommendations
- Renewable energy
- Waste management

**When to Run**: To understand API usage

#### `postman_collection.json`
**Purpose**: Postman API test collection  
**Includes**:
- All endpoint tests
- Example requests
- Error scenarios

**When to Use**: Manual API testing in Postman

---

### Documentation Files

#### `README.md`
**Purpose**: Main project documentation  
**Sections**:
- Overview
- Project structure
- Installation
- API endpoints
- Testing
- Configuration
- Integration
- Deployment

**Audience**: Everyone

#### `QUICKSTART.md`
**Purpose**: 5-minute setup guide  
**Sections**:
- Installation (2 min)
- Configuration (1 min)
- Running (30 sec)
- Testing (1.5 min)
- Next steps

**Audience**: New users

#### `API_DOCS.md`
**Purpose**: Complete API reference  
**Sections**:
- Endpoints
- Request/response formats
- Data models
- Supported intents
- Error codes
- Examples in multiple languages

**Audience**: Developers

#### `DEPLOYMENT.md`
**Purpose**: Deployment guide  
**Sections**:
- Deployment options (Vercel, Render, Railway, etc.)
- Platform-specific guides
- Post-deployment steps
- Security best practices
- Troubleshooting

**Audience**: DevOps, deployment team

#### `PROJECT_OVERVIEW.md`
**Purpose**: Architecture & design document  
**Sections**:
- System architecture
- Data flow
- Technology stack
- Performance metrics
- Security considerations

**Audience**: Stakeholders, team leads

#### `CHECKLIST.md`
**Purpose**: Pre-deployment verification  
**Sections**:
- Implementation checklist
- Testing checklist
- Deployment checklist
- Quality gates

**Audience**: Project manager, QA

#### `FILE_INDEX.md`
**Purpose**: This file - complete file reference  
**Audience**: Developers

---

### Configuration & Setup Files

#### `.env.example`
**Purpose**: Environment variable template  
**Variables**:
- `OPENAI_API_KEY` - OpenAI API key (optional)
- `PORT` - Server port
- `HOST` - Server host
- `ENVIRONMENT` - dev/prod
- `LOG_LEVEL` - Logging level

**When to Use**: Copy to `.env` and fill in values

#### `.gitignore`
**Purpose**: Git ignore rules  
**Ignores**:
- Python cache files
- Virtual environments
- .env files
- Logs
- LTM cache
- IDE files

**When to Edit**: To exclude additional files from git

#### `requirements.txt`
**Purpose**: Python dependencies  
**Key Packages**:
- fastapi - Web framework
- uvicorn - ASGI server
- pydantic - Data validation
- openai - OpenAI API (optional)
- PyYAML - YAML parsing
- httpx - HTTP client

**When to Edit**: When adding new Python packages

#### `setup.ps1`
**Purpose**: Automated setup script for Windows  
**Steps**:
1. Check Python installation
2. Create virtual environment
3. Activate environment
4. Install dependencies
5. Create .env file
6. Create directories

**When to Run**: Initial project setup

---

## 🔍 Quick File Finder

### Need to...

**Change agent behavior?**
→ `agents/workers/sustainability_agent.py`

**Add new API endpoint?**
→ `api.py`

**Modify request/response format?**
→ `communication/models.py`

**Add new intent?**
→ `communication/protocol.py` + `config/agent_config.json`

**Change configuration?**
→ `config/settings.yaml` or `config/agent_config.json`

**Add utility function?**
→ `shared/utils.py`

**Modify caching logic?**
→ `shared/ltm_storage.py`

**Add test?**
→ `test_agent.py`

**Add example?**
→ `examples.py`

**Update documentation?**
→ Appropriate `.md` file

---

## 📊 File Statistics

| Category | Files | Lines of Code (approx) |
|----------|-------|------------------------|
| Core Implementation | 5 | ~800 |
| Communication | 2 | ~150 |
| Configuration | 2 | ~100 |
| Shared Utilities | 2 | ~300 |
| Testing | 3 | ~400 |
| Documentation | 7 | ~2500 (markdown) |
| Setup/Config | 4 | ~100 |
| **Total** | **25** | **~4350** |

---

## 🎯 Critical Files for Deployment

**Must Have**:
1. `api.py` - Main application
2. `main.py` - Entry point
3. `agents/workers/sustainability_agent.py` - Agent logic
4. `communication/models.py` - API models
5. `requirements.txt` - Dependencies
6. `config/agent_config.json` - Registry info

**Should Have**:
- All other Python files
- Configuration files
- Documentation

**Optional for Deployment**:
- Test files
- Example files
- Documentation (but recommended)

---

## 📝 File Modification Frequency

**High Frequency** (modify often):
- `agents/workers/sustainability_agent.py` - Agent improvements
- `config/agent_config.json` - Deployment URLs
- `.env` - Environment-specific settings

**Medium Frequency** (occasional changes):
- `api.py` - New endpoints
- `communication/models.py` - Model updates
- `config/settings.yaml` - Configuration tweaks

**Low Frequency** (rarely change):
- `agents/worker_base.py` - Base class stable
- `shared/ltm_storage.py` - Caching logic stable
- `main.py` - Entry point stable

**Never Change** (reference only):
- Documentation files (update, don't change format)
- `.env.example` (template only)

---

## 🔄 File Dependencies

```
main.py
  ├── api.py
  │   ├── communication/models.py
  │   └── agents/workers/sustainability_agent.py
  │       ├── agents/worker_base.py
  │       ├── shared/ltm_storage.py
  │       └── communication/models.py
  └── shared/utils.py
      └── config/*.yaml
```

---

**Last Updated**: November 2025  
**Total Files**: 25+  
**Project Version**: 1.0.0
