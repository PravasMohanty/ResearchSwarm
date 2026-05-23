# ResearchSwarm 🧠⚡

> A Multi-Agent AI Research Orchestration System built using LangGraph, Gemini 2.5 Flash, Tavily, AsyncIO, and Structured Agent Collaboration.

---

# Table of Contents

1. Introduction
2. System Vision
3. Core Architecture
4. Agent Responsibilities
5. LangGraph Workflow
6. Shared State Architecture
7. Prompt Engineering Strategy
8. Parser Layer
9. Logging & Observability
10. Parallel Research Execution
11. Project Structure
12. Detailed Component Breakdown
13. Installation Guide
14. Environment Variables
15. Running the System
16. Example Workflow
17. Internal Execution Flow
18. Future Improvements
19. Engineering Concepts Used
20. Final Notes

---

# 1. Introduction

ResearchSwarm is a modular multi-agent AI research system designed to autonomously:

- break down complex research objectives,
- perform internet research,
- scrape and synthesize web information,
- analyze findings,
- and generate polished final reports.

The system is orchestrated using LangGraph and follows a graph-based multi-agent architecture.

Instead of relying on a single monolithic LLM prompt, ResearchSwarm distributes responsibilities across specialized AI agents.

---

# 2. System Vision

The project was built around one core idea:

> "How can multiple AI agents coordinate reliably to solve complex objectives?"

The system focuses heavily on:

- modularity,
- orchestration,
- structured state management,
- observability,
- scalability,
- and parser-safe AI communication.

---

# 3. Core Architecture

ResearchSwarm uses a graph-based execution pipeline.

```text
START
  ↓
Planner Agent
  ↓
Research Agents (Parallel)
  ↓
Analyst Agent
  ↓
Writer Agent
  ↓
END
```

---

# 4. Agent Responsibilities

## 4.1 Planner Agent

### Purpose
The Planner Agent decomposes a high-level objective into structured subtasks.

### Responsibilities
- break objectives into atomic tasks
- classify task types
- generate machine-readable task structures
- prepare tasks for orchestration

### Example Output

```json
[
  {
    "title": "Research Cursor pricing",
    "type": "research",
    "description": "Analyze Cursor pricing tiers and offerings."
  },
  {
    "title": "Research GitHub Copilot adoption",
    "type": "research",
    "description": "Analyze GitHub Copilot market adoption and positioning."
  }
]
```

---

## 4.2 Research Agent

### Purpose
The Research Agent gathers grounded factual information from the internet.

### Responsibilities
- Tavily web search
- webpage scraping
- content extraction
- contextual synthesis
- grounded fact generation

### Internal Pipeline

```text
Task
 ↓
Tavily Search
 ↓
Web Scraping
 ↓
Gemini Synthesis
 ↓
Structured Findings
```

### Technologies Used
- Tavily API
- BeautifulSoup
- Requests
- Gemini 2.5 Flash

---

## 4.3 Analyst Agent

### Purpose
The Analyst Agent performs higher-order reasoning over research findings.

### Responsibilities
- detect patterns
- identify contradictions
- extract strategic insights
- analyze risks
- identify trends
- cross-source synthesis

### Why Analyst Agent Exists
ResearchAgent focuses on:
- extraction
- grounding
- factual synthesis

AnalystAgent focuses on:
- reasoning
- interpretation
- strategic understanding

This separation improves architectural clarity.

---

## 4.4 Writer Agent

### Purpose
The Writer Agent converts analyzed intelligence into a polished final report.

### Responsibilities
- executive summary generation
- report structuring
- coherent writing
- section synthesis
- readability optimization

### Output Example

```json
{
  "title": "AI Coding Assistant Market Analysis",
  "executive_summary": "...",
  "sections": [
    {
      "title": "Market Leaders",
      "content": "..."
    }
  ],
  "final_conclusion": "..."
}
```

---

# 5. LangGraph Workflow

The system uses LangGraph for orchestration.

## Graph Flow

```text
START
  ↓
planner_node
  ↓
research_node
  ↓
analyst_node
  ↓
writer_node
  ↓
END
```

## Why LangGraph?

LangGraph provides:

- state-based orchestration
- async graph execution
- node abstraction
- conditional routing support
- graph scalability
- execution tracing
- future cyclic workflows

---

# 6. Shared State Architecture

The entire workflow communicates through a shared state object.

## AgentState

```python
class AgentState(TypedDict):

    objective: str
    session_id: str
    subtasks: List[Dict[str, Any]]
    findings: List[Dict[str, Any]]
    analyzed_findings: Dict[str, Any]
    completed_tasks: List[str]
    current_task: Optional[Dict[str, Any]]
    sources: List[str]
    final_report: Dict[str, Any]
```

## Important Concept

LangGraph nodes return:

```python
{
    "updated_field": value
}
```

instead of mutating and returning the entire state object.

This was an important architectural debugging discovery during development.

---

# 7. Prompt Engineering Strategy

ResearchSwarm heavily relies on structured prompts.

## Core Principles

All prompts are designed to:

- return strict JSON
- avoid markdown
- avoid conversational fluff
- remain parser-friendly
- remain machine-readable

## Why?

LLMs are unreliable when orchestrating systems.

Structured outputs are critical for:
- stability
- parsing
- orchestration
- scalability

---

# 8. Parser Layer

## Purpose
The parser layer stabilizes LLM outputs.

## Why Needed?

LLMs often return:

```text
Sure! Here's the JSON:
```

or malformed outputs.

Without a parser:
- orchestration crashes
- JSON parsing fails
- state becomes corrupted

## Responsibilities
- strip markdown wrappers
- parse JSON safely
- validate outputs
- recover malformed responses

---

# 9. Logging & Observability

ResearchSwarm includes a centralized logging system.

## Log File

```text
logs/research_swarm.log
```

## What Gets Logged

- graph node execution
- planner activity
- research activity
- scraping operations
- parser failures
- final report generation
- workflow completion

## Example Logs

```text
Planner generated 4 subtasks
Research completed for 4 subtasks
Analysis completed
Final report generated
```

## Why Logging Matters

Large AI systems require observability.

Logging helps with:
- debugging
- execution tracing
- monitoring
- production stability

---

# 10. Parallel Research Execution

One of the biggest architectural upgrades was implementing parallel research execution.

## Sequential Problem

Without parallelism:

```text
Task 1 → Task 2 → Task 3
```

Execution becomes slow.

---

## Async Solution

ResearchSwarm uses:

```python
await asyncio.gather(
    *research_coroutines,
    return_exceptions=True
)
```

This allows all research tasks to execute concurrently.

---

## Benefits

- faster execution
- scalable research pipelines
- efficient async orchestration
- improved throughput

---

# 11. Project Structure

```text
backend/
│
├── agents/
│   ├── base_agent.py
│   ├── planner.py
│   ├── researcher.py
│   ├── analyst.py
│   └── writer.py
│
├── prompts/
│   ├── planner_prompt.py
│   ├── researcher_prompt.py
│   ├── analyst_prompt.py
│   └── writer_prompt.py
│
├── orchestrator/
│   ├── graph.py
│   ├── router.py
│   └── workflow.py
│
├── schemas/
│   ├── tasks.py
│   ├── state.py
│   ├── events.py
│   ├── messages.py
│   └── reports.py
│
├── tools/
│   ├── llm.py
│   ├── search.py
│   └── scrapper.py
│
├── utils/
│   ├── parser.py
│   └── logger.py
│
├── config/
│   └── settings.py
│
├── logs/
│
├── main.py
│
└── .env
```

---

# 12. Detailed Component Breakdown

## 12.1 search.py

### Purpose
Wrapper around Tavily search.

### Responsibilities
- perform internet search
- normalize results
- simplify research pipeline

### Output Example

```python
[
    {
        "title": "...",
        "content": "...",
        "url": "..."
    }
]
```

---

## 12.2 scrapper.py

### Purpose
Extract readable webpage content.

### Workflow

```text
URL
 ↓
requests.get()
 ↓
BeautifulSoup
 ↓
remove scripts/styles
 ↓
extract readable text
```

### Important Note
The scraper is NOT AI.
It only extracts webpage text.

---

## 12.3 router.py

### Purpose
Maps task types to graph nodes.

### Current Role
Currently behaves similarly to a dictionary.

Example:

```python
research -> research_node
```

### Future Potential
Later it can support:
- intelligent routing
- dynamic graph transitions
- budget-aware execution
- priority-based routing

---

## 12.4 workflow.py

This file represented the earlier manual orchestration implementation before LangGraph integration.

LangGraph later replaced most orchestration responsibilities.

---

# 13. Installation Guide

## Clone Repository

```bash
git clone <repository-url>
cd ResearchSwarm/backend
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv add langgraph
uv add langchain-google-genai
uv add tavily-python
uv add beautifulsoup4
uv add requests
uv add pydantic-settings
```

---

# 14. Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
MAX_REVISIONS=2
MAX_RESEARCHERS=3
REQUEST_TIMEOUT=30
```

---

# 15. Running the System

```bash
python main.py
```

---

# 16. Example Workflow

## Input Objective

```text
Analyze the current AI coding assistant market including Cursor, Windsurf, Claude Code, and GitHub Copilot.
```

---

## Execution Flow

```text
Planner Agent
    ↓
Creates structured subtasks

Research Agents
    ↓
Perform Tavily searches

Scraper
    ↓
Extracts webpage content

Research Agent
    ↓
Synthesizes findings

Analyst Agent
    ↓
Extracts patterns & strategic insights

Writer Agent
    ↓
Generates polished report
```

---

# 17. Internal Execution Flow

## Step 1 — Graph Starts

LangGraph receives:

```python
initial_state
```

---

## Step 2 — Planner Node

PlannerAgent generates subtasks.

---

## Step 3 — Research Node

Parallel research execution begins.

---

## Step 4 — Analyst Node

Research findings are analyzed.

---

## Step 5 — Writer Node

Final report is synthesized.

---

## Step 6 — END

Final report is returned.

---

# 18. Future Improvements

## Planned Features

- React frontend dashboard
- live event streaming
- human approval layer
- vector database integration
- memory persistence
- citation generation
- retry & recovery system
- PDF/Markdown exports
- multi-model orchestration
- RAG pipelines
- session persistence

---

# 19. Engineering Concepts Used

ResearchSwarm demonstrates:

- Multi-Agent Systems
- Async Orchestration
- Graph-Based Workflows
- Shared State Architectures
- Structured Prompt Engineering
- Parser Stabilization
- Event-Based Observability
- Parallel Async Execution
- Modular System Design
- AI Workflow Engineering

---

# 20. Final Notes

ResearchSwarm was designed not as a chatbot, but as a scalable AI orchestration system.

The project emphasizes:

- architectural clarit