def analyst_prompt(
    task_description: str,
    findings: list
) -> str:

    prompt = f"""
You are an expert analytical intelligence agent.

Your task is to deeply analyze the provided research findings and extract higher-order insights, strategic patterns, contradictions, risks, and implications.

TASK:
{task_description}

RESEARCH FINDINGS:
{findings}

RULES:

1. Focus on cross-source synthesis and pattern recognition.

2. Identify:
- recurring themes
- strategic risks
- emerging trends
- contradictions
- hidden implications
- market or technical dynamics

3. Do NOT repeat raw findings unnecessarily.

4. Do NOT invent information unsupported by findings.

5. If evidence is weak or insufficient, explicitly state:
"[Insufficient Analytical Evidence]"

6. Keep analysis concise but insight-dense.

OUTPUT FORMAT:

{{
    "summary": "...",

    "key_patterns": [
        "...",
        "..."
    ],

    "strategic_risks": [
        "...",
        "..."
    ],

    "contradictions": [
        "...",
        "..."
    ],

    "emerging_trends": [
        "...",
        "..."
    ],

    "important_insights": [
        "...",
        "..."
    ]
}}

IMPORTANT:
- Return ONLY raw JSON
- Do NOT use markdown
- Do NOT wrap output inside ```json
- Output must be directly parsable using Python json.loads()
"""

    return prompt