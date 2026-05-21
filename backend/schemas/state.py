from typing import TypedDict, List, Dict, Any, Optional, Annotated
from operator import add

class AgentState(TypedDict):
    objective: str
    subtasks: List[Dict[str, Any]]
    
    #  FIXED: Annotated goes on the outside, type is 1st argument, reducer is 2nd
    findings: Annotated[List[Dict[str, Any]], add]
    
    analyzed_findings: Dict[str, Any]
    completed_tasks: List[str]
    current_task: Optional[Dict[str, Any]]
    sources: List[str]
    final_report: Dict[str, Any]
    session_id: str