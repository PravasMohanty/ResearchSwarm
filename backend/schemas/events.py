from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime
from enum import Enum


class EventType(str, Enum):

    AGENT_STARTED = "AGENT_STARTED"

    AGENT_COMPLETED = "AGENT_COMPLETED"

    TOOL_CALLED = "TOOL_CALLED"

    THINKING = "THINKING"

    ERROR = "ERROR"

    MESSAGE_SENT = "MESSAGE_SENT"


class AgentEvent(BaseModel):

    session_id: str

    agent_id: str

    event_type: EventType

    payload: Dict[str, Any]

    timestamp: datetime = datetime.utcnow()