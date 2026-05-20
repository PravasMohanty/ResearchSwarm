import json

from typing import Any, Dict, List


class Parser:

    def clean_json_response(
        self,
        response: str
    ) -> str:

        response = response.strip()

        if response.startswith("```json"):
            response = response.replace(
                "```json",
                ""
            )

        if response.endswith("```"):
            response = response[:-3]

        return response.strip()

    def parse_planner_output(
        self,
        response: str
    ) -> List[Dict[str, Any]]:

        try:

            cleaned_response = self.clean_json_response(
                response
            )

            parsed = json.loads(
                cleaned_response
            )

            if not isinstance(parsed, list):
                raise ValueError(
                    "Planner output must be a list"
                )

            return parsed

        except Exception as e:

            print(
                f"[PARSER ERROR - PLANNER]: {e}"
            )

            return []

    def parse_research_output(
        self,
        response: str
    ) -> Dict[str, Any]:

        try:

            cleaned_response = self.clean_json_response(
                response
            )

            parsed = json.loads(
                cleaned_response
            )

            if not isinstance(parsed, dict):
                raise ValueError(
                    "Research output must be a dictionary"
                )

            return parsed

        except Exception as e:

            print(
                f"[PARSER ERROR - RESEARCH]: {e}"
            )

            return {

                "summary": "[Parsing Failed]",

                "key_findings": [],

                "risks_or_limitations": [],

                "contradictions": [],

                "important_insights": []
            }


parser = Parser()