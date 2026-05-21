from agents.base_agent import BaseAgent

from schemas.tasks import Task
from schemas.events import EventType

from prompts.analyst_prompt import analyst_prompt

from tools.llm import llm_manager

from utils.parser import parser


class AnalystAgent(BaseAgent):

    def __init__(self):

        super().__init__(

            agent_id="analyst_1",

            role="analyst"
        )

    async def execute(
        self,
        task: Task,
        findings: list
    ):

        await self.emit_event(

            session_id=task.session_id,

            event_type=EventType.THINKING,

            payload={
                "message": f"Analyzing findings for task: {task.title}"
            }
        )

        prompt = analyst_prompt(

            task_description=task.description,

            findings=findings
        )

        response = await llm_manager.generate(
            prompt
        )

        parsed_response = parser.parse_research_output(
            response
        )

        return parsed_response