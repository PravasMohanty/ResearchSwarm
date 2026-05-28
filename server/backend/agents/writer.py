from agents.base_agent import BaseAgent
from schemas.tasks import Task
from schemas.events import EventType
from prompts.writer_prompt import writer_prompt
from tools.llm import llm_manager
from utils.parser import parser
from utils.logger import logger

class WriterAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            agent_id="writer_1",
            role="writer"
        )

    async def execute(
        self,
        task: Task,
        analyzed_findings: dict
    ):

        logger.info(f"Writing started for task: {task.title}")

        await self.emit_event(
            session_id=task.session_id,
            event_type=EventType.THINKING,
            payload={
                "message": f"Generating final report for: {task.title}"
            }
        )

        prompt = writer_prompt(
            objective=task.description,
            findings=analyzed_findings
        )

        response = await llm_manager.generate(prompt)
        parsed_response = parser.parse_research_output(response)

        logger.info(f"Writing completed for task: {task.title}")

        return parsed_response