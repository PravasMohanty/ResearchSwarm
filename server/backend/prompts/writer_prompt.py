def writer_prompt(
    objective: str,
    findings: list
) -> str:

    prompt = f"""
You are an expert research report writer producing publication-quality, comprehensive reports.

Your task is to generate a thorough, well-structured, and detailed final research report using ALL provided research findings and analysis. The report should read like a professional research paper or in-depth briefing document.

OBJECTIVE:
{objective}

RESEARCH FINDINGS AND ANALYSIS:
{findings}

WRITING GUIDELINES:

1. The report must be COMPREHENSIVE and DETAILED — aim for a substantial document, not a brief summary.

2. Generate AT LEAST 5-7 major sections, each with rich, detailed content.

3. Each section's content must be AT LEAST 3-4 detailed paragraphs (each paragraph 4-6 sentences).

4. Combine overlapping findings intelligently — synthesize, don't just concatenate.

5. Remove redundancy but preserve ALL important details, nuances, and evidence.

6. Include specific data points, statistics, examples, and evidence throughout.

7. Maintain a logical flow: Introduction → Background → Main Analysis → Implications → Future Outlook → Conclusion.

8. For each section, include structured findings with:
   - claim: A specific, evidence-backed assertion (1-2 sentences)
   - evidence: List of supporting data points or facts
   - sources: Referenced source URLs where available
   - confidence: Confidence score between 0.0 and 1.0

9. Write a thorough executive_summary (6-10 sentences) covering all major themes.

10. Write a detailed final_conclusion (5-8 sentences) with forward-looking recommendations.

11. Include ALL sources referenced across the research.

12. Preserve important technical insights, expert opinions, and quantitative data.

13. Use clear, professional, and engaging prose — avoid jargon-heavy or overly academic language.

OUTPUT FORMAT:

{{
    "title": "A descriptive, engaging title for the research report",

    "executive_summary": "A comprehensive 6-10 sentence executive summary covering the key themes, major findings, critical risks, and primary conclusions of the research.",

    "sections": [
        {{
            "title": "Section Title",
            "content": "Detailed, multi-paragraph section content (at least 3-4 paragraphs, each 4-6 sentences). Include specific data, examples, and evidence. This should be substantial and informative.",
            "findings": [
                {{
                    "claim": "A specific claim supported by the research",
                    "evidence": ["Supporting data point 1", "Supporting data point 2"],
                    "sources": ["https://source-url.com"],
                    "confidence": 0.85
                }}
            ]
        }}
    ],

    "final_conclusion": "A detailed 5-8 sentence conclusion summarizing the research implications, key takeaways, and actionable recommendations for stakeholders.",

    "sources": ["https://all-referenced-sources.com"]
}}

IMPORTANT:
- Return ONLY raw JSON
- Do NOT use markdown
- Output must be parsable using Python json.loads()
- DEPTH and DETAIL are essential — a short or superficial report is not acceptable
- Each section should be substantial enough to stand on its own as a mini-report
"""

    return prompt