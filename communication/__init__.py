"""
Communication package for multi-agent message passing.
Contains models and protocols for standardized communication.
"""

__version__ = "1.0.0"

from .models import (
    Status,
    Role,
    Message,
    AgentRequest,
    AgentResponse,
    HealthCheckResponse
)

from .protocol import (
    MessageType,
    TaskPriority,
    AgentStatus,
    SUSTAINABILITY_INTENTS
)

__all__ = [
    "Status",
    "Role",
    "Message",
    "AgentRequest",
    "AgentResponse",
    "HealthCheckResponse",
    "MessageType",
    "TaskPriority",
    "AgentStatus",
    "SUSTAINABILITY_INTENTS"
]
