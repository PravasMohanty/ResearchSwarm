import asyncio
from orchestrator.graph import graph
from utils.logger import logger

async def main():

    initial_state = {
        "objective": "Analyze the current AI coding assistant market including Cursor, Windsurf, Claude Code, and GitHub Copilot.",
        "subtasks": [],
        "findings": [],
        "analyzed_findings": {},
        "completed_tasks": [],
        "current_task": None,
        "sources": [],
        "final_report": {},
        "session_id": ""
    }

    logger.info("ResearchSwarm execution started")

    result = await graph.ainvoke(
        initial_state
    )

    report = result["final_report"]

    logger.info("ResearchSwarm execution completed")

    print("\n========== FINAL REPORT ==========\n")
    print(f"Title: {report.get('title', 'N/A')}\n")
    print(f"Executive Summary:\n{report.get('executive_summary', 'N/A')}\n")

    for section in report.get("sections", []):
        print(f"--- {section.get('title', 'Section')} ---")
        print(f"{section.get('content', '')}\n")

    print(f"Final Conclusion:\n{report.get('final_conclusion', 'N/A')}\n")


if __name__ == "__main__":
    asyncio.run(main())