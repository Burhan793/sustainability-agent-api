"""
FastAPI application for Sustainability Footprint Agent.
Provides REST API endpoints following the SPM project standards.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import sys
import os
from typing import Dict, Any
import time

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from communication.models import (
    AgentRequest, 
    AgentResponse, 
    Status, 
    HealthCheckResponse
)
from agents.workers.sustainability_agent import SustainabilityFootprintAgent

# Initialize FastAPI app
app = FastAPI(
    title="Sustainability Footprint Agent",
    description="AI Agent for environmental impact analysis and sustainability assessment",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the agent
agent = SustainabilityFootprintAgent()

# Agent configuration
AGENT_NAME = "sustainability-footprint-agent"
REQUEST_TIMEOUT = 30  # seconds


@app.middleware("http")
async def timeout_middleware(request: Request, call_next):
    """Add timeout to all requests."""
    start_time = time.time()
    try:
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "agent_name": AGENT_NAME,
                "status": "error",
                "data": None,
                "error_message": f"Internal server error: {str(e)}"
            }
        )


@app.get("/api/sustainability-footprint-agent/health")
async def health_check() -> HealthCheckResponse:
    """
    Health check endpoint.
    Returns the agent's operational status.
    """
    return HealthCheckResponse(
        status="ok",
        agent_name=AGENT_NAME,
        ready=True
    )


@app.post("/api/sustainability-footprint-agent")
async def process_request(request: AgentRequest) -> AgentResponse:
    """
    Main endpoint for processing sustainability-related queries.
    
    Args:
        request: AgentRequest with messages
        
    Returns:
        AgentResponse with analysis results
    """
    try:
        # Validate request
        if not request.messages:
            raise HTTPException(
                status_code=400,
                detail="No messages provided in request"
            )
        
        # Convert Pydantic models to dictionaries for agent processing
        messages = [msg.dict() for msg in request.messages]
        
        # Process request with timeout consideration
        result = agent.process_api_request(messages)
        
        # Return successful response
        return AgentResponse(
            agent_name=AGENT_NAME,
            status=Status.SUCCESS,
            data=result,
            error_message=None
        )
    
    except HTTPException as he:
        # Re-raise HTTP exceptions
        raise he
    
    except Exception as e:
        # Catch all other errors and return error response
        print(f"[{AGENT_NAME}] Error processing request: {e}")
        return AgentResponse(
            agent_name=AGENT_NAME,
            status=Status.ERROR,
            data=None,
            error_message=str(e)
        )


@app.get("/")
async def root():
    """Root endpoint with agent information."""
    return {
        "agent_name": AGENT_NAME,
        "description": "Sustainability Footprint Agent - Environmental impact analysis and sustainability assessment",
        "version": "1.0.0",
        "endpoints": {
            "main": "/api/sustainability-footprint-agent",
            "health": "/api/sustainability-footprint-agent/health"
        },
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


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler to ensure we always return proper JSON."""
    return JSONResponse(
        status_code=500,
        content={
            "agent_name": AGENT_NAME,
            "status": "error",
            "data": None,
            "error_message": f"Unexpected error: {str(exc)}"
        }
    )


if __name__ == "__main__":
    import uvicorn
    
    # Get port from environment or use default
    port = int(os.getenv("PORT", 8000))
    
    print(f"\n{'='*60}")
    print(f"Starting {AGENT_NAME}")
    print(f"{'='*60}")
    print(f"Health Check: http://localhost:{port}/api/sustainability-footprint-agent/health")
    print(f"Main Endpoint: http://localhost:{port}/api/sustainability-footprint-agent")
    print(f"{'='*60}\n")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
