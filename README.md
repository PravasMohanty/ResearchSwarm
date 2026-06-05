# 🐝 ResearchSwarm

ResearchSwarm is a multi-agent AI research system that automatically decomposes complex research questions into smaller tasks, conducts parallel research, synthesizes findings, and generates comprehensive reports.

Instead of relying on a single AI model to answer broad questions, ResearchSwarm orchestrates a swarm of specialized agents that collaborate to produce structured, evidence-based research outputs.

---

## 🚀 Problem Statement

Conducting high-quality research is time-consuming.

Users often spend hours:

* Searching across multiple sources
* Comparing conflicting information
* Organizing findings
* Synthesizing conclusions

ResearchSwarm automates this workflow by creating a coordinated team of AI agents that work together to perform deep research.

---

## ✨ Features

* Multi-Agent Research Workflow
* Automatic Task Decomposition
* Parallel Research Execution
* AI-Powered Analysis & Synthesis
* Structured Report Generation
* Research History Tracking
* Authentication Support
* Dockerized Deployment
* Real-Time Execution Logging

---

## 🏗️ System Architecture

```text
User Query
     │
     ▼
┌─────────────┐
│ Planner AI  │
└─────────────┘
     │
     ▼
Research Subtasks
     │
     ▼
┌─────────────────────────────┐
│ Parallel Research Agents    │
└─────────────────────────────┘
     │
     ▼
Research Findings
     │
     ▼
┌─────────────┐
│ Analyst AI  │
└─────────────┘
     │
     ▼
Final Report
```

### Planner Agent

Breaks complex research objectives into focused subtasks.

### Research Agents

Execute parallel investigations and gather information from multiple sources.

### Analyst Agent

Combines research outputs and identifies key insights.

### Report Generator

Produces a structured final report for the user.

---

## 🛠 Tech Stack

### Frontend

* React
* Vite
* JavaScript

### Backend

* FastAPI
* Python

### AI & Orchestration

* LangGraph
* Google Gemini
* Tavily Search

### Deployment

* Docker
* Docker Hub
* Render
* Vercel

---

## 📂 Project Structure

```text
ResearchSwarm
│
├── frontend
│   ├── src
│   └── public
│
├── server
│   ├── backend
│   │   ├── agents
│   │   ├── api
│   │   ├── config
│   │   ├── orchestrator
│   │   ├── prompts
│   │   ├── schemas
│   │   ├── services
│   │   ├── tools
│   │   ├── utils
│   │   └── results
│   │
│   ├── pyproject.toml
│   └── uv.lock
│
├── Dockerfile.backend
├── Dockerfile.frontend
└── README.md
```

---

## 🔄 Workflow

1. User submits a research query.
2. Planner Agent generates subtasks.
3. Research Agents execute tasks in parallel.
4. Results are aggregated.
5. Analyst Agent synthesizes findings.
6. Final report is generated.
7. Research history is stored for future access.

---

## 📜 Logging & Observability

ResearchSwarm provides detailed execution logs for monitoring and debugging.

Logs include:

* Planner execution
* Research task creation
* Search operations
* Agent outputs
* Report generation
* Error tracking
* Workflow execution status

All execution logs can be monitored directly from the backend/server side.

---

## 🔐 Authentication

ResearchSwarm includes authentication support for securing research operations.

Supported endpoints:

```http
POST /auth/login
POST /research/start
GET  /research/history
GET  /research/history/{filename}
```

---

## 🌐 Deployment

### Frontend

Hosted on Vercel.

### Backend

Hosted on Render using Docker.

### Docker Hub

Backend images are published and deployed through Docker Hub.

---

## ⚙️ Environment Variables

```env
GEMINI_API_KEY=your_key
TAVILY_API_KEY=your_key

APP_USERNAME=admin
APP_PASSWORD=password
```

---

## ▶️ Running Locally

### Backend

```bash
cd server

uv sync

cd backend

uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 🧪 Example Research Questions

### Economics

```text
Will India become a developed economy by 2047?
```

### Climate

```text
Can renewable energy completely replace fossil fuels by 2050?
```

### Healthcare

```text
What are the biggest challenges facing global healthcare systems over the next 20 years?
```

### Space Exploration

```text
Is a permanent human settlement on Mars feasible within this century?
```

## Acknowledgements

ResearchSwarm was developed with the assistance of large language models, primarily ChatGPT and Claude, which were used as development companions throughout the project.

These tools were leveraged for discussing architectural trade-offs, reviewing implementation approaches, debugging issues, refining documentation, and accelerating routine development tasks. Their role was similar to that of an interactive technical reference or pair-programming assistant.

The conception of the project, system architecture, orchestration workflow, agent design, implementation decisions, integration, deployment, testing, and overall direction of the project were carried out by the author.

The project also builds upon the broader open-source ecosystem, particularly FastAPI, React, LangGraph, Docker, and Tavily, whose tools and communities made the development of ResearchSwarm possible.


---

## 🎯 Future Enhancements

* Citation Verification
* User Accessible logs of entire process
* Multi-Model Agent Collaboration
* Source Reliability Scoring
* Real-Time Agent Visualization
* Export to PDF and DOCX
* Collaborative Research Workspaces

---

## 👨‍💻 Author

Pravas Mohantyfut

Computer Science Engineering Student

ResearchSwarm was built to demonstrate how multi-agent systems can transform complex research workflows through intelligent task decomposition, parallel execution, and AI-driven synthesis.
