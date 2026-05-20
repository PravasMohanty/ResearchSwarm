def researcher_prompt(
    task_description: str,
    context: str
) -> str:

    prompt = f"""
You are an expert research agent.

Your job is to analyze the provided web context and extract accurate, grounded, and useful findings related to the assigned task.

TASK:
{task_description}

WEB CONTEXT:
{context}

RULES:

1. Every important claim MUST be grounded in the provided context.

2. If sufficient information is unavailable, explicitly state:
"[Insufficient Data]"

3. Ignore:
- advertisements
- marketing fluff
- repetitive statements
- irrelevant sections

4. Highlight:
- important facts
- technical details
- risks
- contradictions
- limitations
- trends

5. Do NOT invent information.

6. Keep findings concise but information-dense.

7. Focus only on information relevant to the assigned task.

OUTPUT FORMAT:

{
    "summary": "...",

    "key_findings": [
        "...",
        "..."
    ],

    "risks_or_limitations": [
        "...",
        "..."
    ],

    "contradictions": [
        "...",
        "..."
    ],

    "important_insights": [
        "...",
        "..."
    ]
}

Return ONLY valid JSON.
"""

    return prompt