from abc import ABC, abstractmethod

from schemas.tasks import Task

from schemas.events import AgentEvent, EventType


class BaseAgent(ABC):

    def __init__(

        self,
        agent_id: str,
        role: str
    ):

        self.agent_id = agent_id
        self.role = role

    async def emit_event(

        self,
        session_id: str,
        event_type: EventType,
        payload: dict
    ):

        event = AgentEvent(

            session_id=session_id,
            agent_id=self.agent_id,
            event_type=event_type,
            payload=payload
        )

        print(f"\n[EVENT] {event}\n")

    @abstractmethod
    async def execute(

        self,
        task: Task
    ):

        pass