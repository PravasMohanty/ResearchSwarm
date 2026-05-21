import uuid
import asyncio
from langgraph.graph import StateGraph, START, END

from schemas.state import AgentState
from schemas.tasks import Task, TaskStatus
from utils.logger import logger
from agents.planner import PlannerAgent
from agents.researcher import ResearcherAgent
from agents.analyst import AnalystAgent
from agents.writer import WriterAgent


planner_agent = PlannerAgent()
research_agent = ResearcherAgent()
analyst_agent = AnalystAgent()
writer_agent = WriterAgent()


async def planner_node(state: AgentState):
    logger.info("Entering planner node")
    session_id = str(uuid.uuid4())

    root_task = Task(
        task_id=str(uuid.uuid4()),
        session_id=session_id,
        title="Root Task",
        description=state["objective"],
        status=TaskStatus.PENDING,
        priority=1
    )

    subtasks = await planner_agent.execute(
        root_task
    )

    state["subtasks"] = subtasks
    state["session_id"] = session_id

    logger.info(f"Planner generated {len(subtasks)} subtasks")

    return state


async def research_node(state: AgentState):

    research_coroutines = []

    for subtask in state["subtasks"]:

        task = Task(
            task_id=str(uuid.uuid4()),
            session_id=state["session_id"],
            title=subtask["title"],
            description=subtask["description"],
            status=TaskStatus.PENDING,
            priority=1
        )

        coroutine = research_agent.execute(
            task
        )

        research_coroutines.append(
            coroutine
        )

    findings = await asyncio.gather(
    *research_coroutines,
    return_exceptions=True
)

    valid_findings = []

for result in findings:

    if isinstance(result, Exception):

        logger.error(str(result))

        continue

    valid_findings.append(result)

state["findings"] = valid_findings

    logger.info(f"Research completed for {len(findings)} subtasks")


    return state


async def analyst_node(state: AgentState):
    logger.info("Entering analyst node")
    task = Task(
        task_id=str(uuid.uuid4()),
        session_id=state["session_id"],
        title="Analysis Task",
        description=state["objective"],
        status=TaskStatus.PENDING,
        priority=1
    )

    analyzed_findings = await analyst_agent.execute(
        task,
        state["findings"]
    )

    state["analyzed_findings"] = analyzed_findings

    logger.info("Analysis completed")

    return state


async def writer_node(state: AgentState):
    logger.info("Entering writer node")
    task = Task(
        task_id=str(uuid.uuid4()),
        session_id=state["session_id"],
        title="Writer Task",
        description=state["objective"],
        status=TaskStatus.PENDING,
        priority=1
    )

    final_report = await writer_agent.execute(
        task,
        state["analyzed_findings"]
    )

    state["final_report"] = final_report

    logger.info("Final report generated")

    return state


graph_builder = StateGraph(
    AgentState
)

graph_builder.add_node(
    "planner_node",
    planner_node
)

graph_builder.add_node(
    "research_node",
    research_node
)

graph_builder.add_node(
    "analyst_node",
    analyst_node
)

graph_builder.add_node(
    "writer_node",
    writer_node
)

graph_builder.add_edge(
    START,
    "planner_node"
)

graph_builder.add_edge(
    "planner_node",
    "research_node"
)

graph_builder.add_edge(
    "research_node",
    "analyst_node"
)

graph_builder.add_edge(
    "analyst_node",
    "writer_node"
)

graph_builder.add_edge(
    "writer_node",
    END
)

graph = graph_builder.compile()