"""
Main entry point for the Sustainability Footprint Agent.
Runs the FastAPI server and initializes the agent system.
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from api import app
import uvicorn
from shared.utils import setup_logging, ConfigLoader


def main():
    """Main entry point for the application."""
    
    # Setup logging
    logger = setup_logging(log_level="INFO")
    logger.info("Starting Sustainability Footprint Agent...")
    
    # Load configuration
    config_dir = os.path.join(project_root, "config")
    config_loader = ConfigLoader(config_dir)
    settings, agent_config = config_loader.load_all()
    
    # Get API configuration
    api_config = settings.get("api", {})
    host = api_config.get("host", "0.0.0.0")
    port = int(os.getenv("PORT", api_config.get("port", 8000)))
    
    # Log startup information
    logger.info(f"{'='*60}")
    logger.info(f"Sustainability Footprint Agent")
    logger.info(f"{'='*60}")
    logger.info(f"Host: {host}")
    logger.info(f"Port: {port}")
    logger.info(f"Health Check: http://localhost:{port}/api/sustainability-footprint-agent/health")
    logger.info(f"Main Endpoint: http://localhost:{port}/api/sustainability-footprint-agent")
    logger.info(f"{'='*60}")
    
    # Run the server
    uvicorn.run(
        "api:app",
        host=host,
        port=port,
        reload=False,  # Set to True for development
        log_level="info"
    )


if __name__ == "__main__":
    main()
