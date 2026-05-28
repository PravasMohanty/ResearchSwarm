from agents.base_agent import BaseAgent
from schemas.tasks import Task
from schemas.events import EventType
from tools.llm import llm_manager
from tools.search import search_manager
from tools.scraper import scraper
from utils.parser import parser
from prompts.researcher_prompt import researcher_prompt
from utils.logger import logger

class ResearcherAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            agent_id="researcher_1",
            role="researcher"
        )

    async def execute(
        self,
        task : Task
    ):
        logger.info(f"Research started for task: {task.title}")

        await self.emit_event(
            session_id=task.session_id,
            event_type=EventType.THINKING,
            payload={
                "message": f"Researching on task: {task.title}"
            }
        )
        logger.info(f"Research started for task: {task.title}")

        search_results = await search_manager.search(

            query=task.description,
            max_results=5
        )

        scraped_context = ""
        sources = []

        for result in search_results:

            scraped_data = await scraper.scrape(
                result["url"]
            )

            scraped_context += f"""

Title:
{result['title']}

Content:
{scraped_data['content']}

Source:
{result['url']}

"""
            sources.append(result["url"])

        prompt = researcher_prompt(
            task_description=task.description,
            context=scraped_context
        )

        logger.info(f"Retrieved {len(search_results)} search results")

        findings = await llm_manager.generate(prompt)

        parsed_findings = parser.parse_research_output(findings)

        logger.info(f"Research completed for task: {task.title}")

        return parsed_findings

