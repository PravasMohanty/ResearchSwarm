from typing import TypedDict, List, Dict, Any, Optional


class AgentState(TypedDict):
    objective: str
    subtasks: List[Dict[str, Any]]
    findings: List[Dict[str, Any]]
    analyzed_findings: Dict[str, Any]
    completed_tasks: List[str]
    current_task: Optional[Dict[str, Any]]
    sources: List[str]
    final_report: Dict[str, Any]