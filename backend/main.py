import asyncio
from orchestrator.graph import graph
from utils.logger import logger

async def main():

    initial_state = {
        "objective": "Which companies declared very good results in terms of profitability in the last quarter?",
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

    # =========================
    # CREATE REPORT TEXT
    # =========================
    output = "\n========== FINAL REPORT ==========\n\n"

    output += f"Title: {report.get('title', 'N/A')}\n\n"

    output += (
        f"Executive Summary:\n"
        f"{report.get('executive_summary', 'N/A')}\n\n"
    )

    for section in report.get("sections", []):
        output += f"--- {section.get('title', 'Section')} ---\n"
        output += f"{section.get('content', '')}\n\n"

    output += (
        f"Final Conclusion:\n"
        f"{report.get('final_conclusion', 'N/A')}\n"
    )

    # =========================
    # PRINT TO TERMINAL
    # =========================
    print(output)

    # =========================
    # SAVE TO TEXT FILE
    # =========================
    with open("results/final_report.txt", "w", encoding="utf-8") as f:
        f.write(output)

    print("Report saved to final_report.txt")


if __name__ == "__main__":
    asyncio.run(main())