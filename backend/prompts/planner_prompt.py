def planner_prompt(task_description: str) -> str:

    prompt = f"""
You are a world-class research planning strategist.

Your responsibility is to decompose a complex research objective into a comprehensive set of structured, executable subtasks for a multi-agent orchestration system. The goal is to produce an exhaustive, deeply researched final report.

OBJECTIVE:
{task_description}

PLANNING GUIDELINES:

1. Generate between 5 and 8 highly specific subtasks to ensure broad and deep coverage of the objective.

2. Each subtask must target a DISTINCT angle, perspective, or dimension of the objective. Think about:
   - Historical context and background
   - Current state and recent developments
   - Key players, stakeholders, or entities involved
   - Technical or scientific details
   - Real-world applications, case studies, or examples
   - Challenges, risks, controversies, and criticisms
   - Future outlook, predictions, and emerging trends
   - Statistical data, market analysis, or quantitative evidence

3. Each subtask must represent exactly ONE actionable, focused research responsibility.

4. Subtask descriptions must be detailed (2-3 sentences minimum) explaining exactly what to investigate and what kind of information to extract.

5. Avoid overlapping or duplicate subtasks.

6. Valid task types are:
   - research
   - analysis
   - writer
   - critic
   - coding

7. Every subtask dictionary MUST contain:
   - title (descriptive, specific)
   - type (one of the valid types above)
   - description (detailed, 2-3 sentences)

8. Return ONLY a valid JSON array of objects.

9. Do NOT return markdown, explanations, or code blocks.

10. Do NOT include comments or trailing commas.

OUTPUT FORMAT EXAMPLE:

[
    {{
        "title": "Historical Evolution of Quantum Computing",
        "type": "research",
        "description": "Research the complete historical timeline of quantum computing from theoretical foundations to modern developments. Cover key milestones, breakthrough experiments, pivotal research papers, and the evolution of quantum hardware architectures."
    }},
    {{
        "title": "Current Industry Leaders and Their Approaches",
        "type": "research",
        "description": "Investigate the major companies and institutions leading quantum computing development including IBM, Google, Microsoft, IonQ, and academic labs. Compare their technical approaches, qubit technologies, and strategic roadmaps."
    }},
    {{
        "title": "Comparative Analysis of Competing Technologies",
        "type": "analysis",
        "description": "Analyze and compare superconducting qubits, trapped ions, photonic quantum computing, and topological qubits. Evaluate each approach's strengths, weaknesses, scalability potential, and current error rates."
    }}
]

IMPORTANT:
- Return ONLY raw JSON
- Output must be directly parsable using Python json.loads()
- Generate AT LEAST 5 subtasks for comprehensive coverage

NOW GENERATE THE SUBTASKS.
"""

    return prompt