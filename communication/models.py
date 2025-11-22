"""
Pydantic models for communication between agents.
Defines the request and response formats for all agents.
"""

from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from enum import Enum


class Status(str, Enum):
    """Status enumeration for agent responses"""
    SUCCESS = "success"
    ERROR = "error"


class Role(str, Enum):
    """Role enumeration for message sender"""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class Message(BaseModel):
    """Individual message in a conversation"""
    role: Role
    content: str


class AgentRequest(BaseModel):
    """
    Standard request format for all agents.
    Contains a list of messages representing the conversation history.
    """
    messages: List[Message]


class AgentResponse(BaseModel):
    """
    Standard response format for all agents.
    Must be used by every agent to ensure consistency.
    """
    agent_name: str
    status: Status
    data: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None


class HealthCheckResponse(BaseModel):
    """Standard health check response"""
    status: str
    agent_name: str
    ready: bool
