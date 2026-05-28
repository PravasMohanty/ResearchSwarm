import uuid
from agents.planner import PlannerAgent
from agents.research_agent import ResearchAgent
from schemas.tasks import Task, TaskStatus


class WorkflowOrchestrator:

    def __init__(self):
        self.planner_agent = PlannerAgent()
        self.research_agent = ResearchAgent()

    async def orchestrate(
        self,
        objective: str
    ):

        session_id = str(uuid.uuid4())

        root_task = Task(
            task_id=str(uuid.uuid4()),
            session_id=session_id,
            title="Root Task",
            description=objective,
            status=TaskStatus.PENDING,
            priority=1
        )

        print("\n[WORKFLOW STARTED]\n")
        print(f"Root Task:\n{root_task}\n")

        subtasks = await self.planner_agent.execute(
            root_task
        )

        print("\n[SUBTASKS GENERATED]\n")
        print(subtasks)

        all_results = []

        for subtask in subtasks:

            task_type = subtask.get(
                "type",
                "research"
            )

            task_title = subtask.get(
                "title",
                "Untitled Task"
            )

            task = Task(

                task_id=str(uuid.uuid4()),
                session_id=session_id,
                title=task_title,
                description=task_title,
                status=TaskStatus.PENDING,
                priority=1
            )

            result = None

            if task_type == "research":

                result = await self.research_agent.execute(
                    task
                )

            if result:
                all_results.append(result)

        print("\n[ALL TASKS COMPLETED]\n")

        return {

            "session_id": session_id,
            "objective": objective,
            "results": all_results
        }