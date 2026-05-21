from agents.researcher import ResearcherAgent


class Dispatcher:

    def __init__(self):

        self.research_agent = ResearcherAgent()

    async def dispatch(
        self,
        task_type: str,
        task
    ):

        if task_type == "research":

            return await self.research_agent.execute(
                task
            )

        raise ValueError(
            f"Unsupported task type: {task_type}"
        )


dispatcher = Dispatcher()