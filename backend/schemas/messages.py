from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from datetime import datetime
from enum import Enum

class MessageType(str, Enum):
    TASK_ASSIGNMENT = "task_assignment"
    TASK_RESULT = "task_result"
    STATUS_UPDATE = "status_update"
    REVISON_REQUEST = "revision_request"
    TOOL_CALL = "tool_call"
    THINKING = "thinking"
    ERROR = "error"
    FINAL_REPORT = "final_report"

class AgentMessage(BaseModel):
    session_id: str
    task_id: str
    sender: str
    receiver: str
    message_type: MessageType
    content: Dict[str, Any]
    timestamp: datetime = datetime.utcnow()
    metadata: Optional[Dict[str, Any]] = None