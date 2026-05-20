from agents.base_agent import BaseAgent
from schemas.tasks import Task
from schemas.events import EventType
from tools.llm import llm_manager
from prompts.planner_prompt import PlannerPrompt

class PlannerAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            agent_id="planner_1",
            role="planner"
        )

    async def execute(

        self,
        task: Task
    ):

        await self.emit_event(

            session_id=task.session_id,
            event_type=EventType.THINKING,
            payload={
                "message": "Planning subtasks..."
            }
        )

        prompt = PlannerPrompt(task.description)

        response = await llm_manager.generate(prompt)

        return response