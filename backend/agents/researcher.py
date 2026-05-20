from agents.base_agent import BaseAgent
from schemas.tasks import Task
from schemas.events import EventType
from tools.llm import llm_manager
from tools.search import search_manager
from tools.scraper import scraper
from utils.parser import parser

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
        await self.emit_event(
            self,
            session_id = Task.session_id,
            event_type=EventType.THINKING,
            payload={
                "message": f"Researching on task: {task.title}"
            }
        )

        search_results = await search_manager.search(

            query=task.description,
            max_results=3
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

        findings = await llm_manager.generate(prompt)

        parsed_findings = parser.parse_research_output(findings)

        return parsed_findings

