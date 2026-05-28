import os
import json
import re
from datetime import datetime, timezone
from orchestrator.graph import graph
from utils.logger import logger


# Absolute path to backend/results/ regardless of CWD
RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")


def _sanitize_filename(text: str, max_len: int = 60) -> str:
    """Create a filesystem-safe slug from a query string."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)      # remove special chars
    text = re.sub(r"[\s_]+", "_", text)        # collapse whitespace to _
    text = text.strip("_")
    return text[:max_len]


def _build_filename(query: str) -> str:
    """Generate a unique filename: YYYYMMDD_HHMMSS__query_slug.json"""
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    slug = _sanitize_filename(query)
    return f"{ts}__{slug}.json"


async def run_research(objective: str):

    initial_state = {
        "objective": objective,
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

    result = await graph.ainvoke(initial_state)

    report = result["final_report"]

    logger.info("ResearchSwarm execution completed")

    # ---- Build readable text output ----
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

    # ---- Persist to results/ ----
    os.makedirs(RESULTS_DIR, exist_ok=True)

    filename = _build_filename(objective)
    filepath = os.path.join(RESULTS_DIR, filename)

    history_entry = {
        "query": objective,
        "raw_report": report,
        "report_text": output,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(history_entry, f, indent=2, ensure_ascii=False, default=str)

    logger.info(f"Report saved to {filepath}")

    # Also keep the legacy text file for backwards compat
    with open(os.path.join(RESULTS_DIR, "final_report.txt"), "w", encoding="utf-8") as f:
        f.write(output)

    return {
        "report": output,
        "raw_report": report,
        "filename": filename,
    }