"""
Communication protocol constants and message types.
Defines standard message types and protocols for inter-agent communication.
"""

from enum import Enum


class MessageType(str, Enum):
    """Message types for supervisor-worker communication"""
    TASK_ASSIGNMENT = "task_assignment"
    COMPLETION_REPORT = "completion_report"
    STATUS_UPDATE = "status_update"
    ERROR_REPORT = "error_report"


class TaskPriority(int, Enum):
    """Task priority levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class AgentStatus(str, Enum):
    """Agent operational status"""
    IDLE = "IDLE"
    BUSY = "BUSY"
    OFFLINE = "OFFLINE"
    ERROR = "ERROR"


# Standard intents for the Sustainability Footprint Agent
SUSTAINABILITY_INTENTS = [
    "carbon_footprint_analysis",
    "energy_consumption_tracking",
    "waste_management_assessment",
    "sustainability_metrics",
    "environmental_impact_analysis",
    "green_building_assessment",
    "renewable_energy_recommendations"
]
