"""
Shared utility functions for the Multi-Agent System.
Provides logging, time utilities, and helper functions.
"""

import logging
import os
from datetime import datetime
from typing import Optional
import yaml
import json


def setup_logging(log_level: str = "INFO", log_file: Optional[str] = None) -> logging.Logger:
    """
    Set up logging configuration.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file path
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger("MultiAgentSystem")
    logger.setLevel(getattr(logging, log_level.upper()))
    
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(name)s - %(message)s"
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def load_yaml_config(config_path: str) -> dict:
    """
    Load YAML configuration file.
    
    Args:
        config_path: Path to YAML config file
        
    Returns:
        Configuration dictionary
    """
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading YAML config: {e}")
        return {}


def load_json_config(config_path: str) -> dict:
    """
    Load JSON configuration file.
    
    Args:
        config_path: Path to JSON config file
        
    Returns:
        Configuration dictionary
    """
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON config: {e}")
        return {}


def get_timestamp() -> str:
    """
    Get current timestamp in ISO format.
    
    Returns:
        ISO formatted timestamp string
    """
    return datetime.utcnow().isoformat() + "Z"


def validate_api_key(api_key: Optional[str]) -> bool:
    """
    Validate API key format.
    
    Args:
        api_key: API key to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not api_key:
        return False
    return len(api_key) > 20  # Basic validation


def sanitize_query(query: str) -> str:
    """
    Sanitize user query for processing.
    
    Args:
        query: Raw user query
        
    Returns:
        Sanitized query string
    """
    return query.strip()


def format_error_message(error: Exception) -> str:
    """
    Format error message for user display.
    
    Args:
        error: Exception object
        
    Returns:
        Formatted error message
    """
    return f"{type(error).__name__}: {str(error)}"


def ensure_directory(directory_path: str) -> None:
    """
    Ensure directory exists, create if not.
    
    Args:
        directory_path: Path to directory
    """
    os.makedirs(directory_path, exist_ok=True)


class ConfigLoader:
    """Configuration loader utility class."""
    
    def __init__(self, config_dir: str):
        """
        Initialize config loader.
        
        Args:
            config_dir: Directory containing config files
        """
        self.config_dir = config_dir
        self.settings = None
        self.agent_config = None
    
    def load_all(self) -> tuple:
        """
        Load all configuration files.
        
        Returns:
            Tuple of (settings, agent_config)
        """
        settings_path = os.path.join(self.config_dir, "settings.yaml")
        agent_config_path = os.path.join(self.config_dir, "agent_config.json")
        
        self.settings = load_yaml_config(settings_path)
        self.agent_config = load_json_config(agent_config_path)
        
        return self.settings, self.agent_config
    
    def get_agent_config(self, agent_name: str) -> Optional[dict]:
        """
        Get configuration for specific agent.
        
        Args:
            agent_name: Name of the agent
            
        Returns:
            Agent configuration dictionary or None
        """
        if not self.agent_config:
            self.load_all()
        
        return self.agent_config.get(agent_name)
