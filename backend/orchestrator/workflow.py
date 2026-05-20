import uuid
from agents.planner import PlannerAgent
from schemas.tasks import Task, TaskStatus


class WorkflowOrchestrator:

    def __init__(self):
        self.planner_agent = PlannerAgent()

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

        print(f"\n[WORKFLOW STARTED]\n")
        print(f"Root Task:\n{root_task}\n")

        subtasks = await self.planner_agent.execute(root_task)

        print(f"\n[SUBTASKS GENERATED]\n")
        print(subtasks)

        return subtasks