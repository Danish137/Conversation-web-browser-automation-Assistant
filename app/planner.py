# app/planner.py

import requests
from typing import Any
import json
import re
from app.schemas import Plan, PlanRequest
from app.config import Config
from pydantic import ValidationError


class Planner:
    def __init__(self):
        self.api_key = Config.OPENROUTER_API_KEY
        self.model = Config.MODEL_NAME
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"


    def generate_plan(self, user_input: str) -> Plan:
        prompt = self._build_prompt(user_input)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an action planner. Respond ONLY with a JSON plan."},
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )

        content = response.choices[0].message.content

        try:
            json_obj = json.loads(content)
            plan = Plan.model_validate(json_obj)

            # Normalize modifiers: list[str] ➡️ single str (optional, depends on executor logic)
            for step in plan.steps:
                if step.params.modifiers and isinstance(step.params.modifiers, list):
                    step.params.modifiers = " ".join(step.params.modifiers)

            return plan

        except (json.JSONDecodeError, ValidationError) as e:
            raise ValueError(f"Invalid JSON from LLM: {e}\n\nResponse:\n{content}")

    def _build_prompt(self, command: str) -> str:
        return f"""
Convert the following command into a JSON action plan.

Command: "{command}"

Respond ONLY with a valid JSON in the following format:

{{
  "steps": [
    {{"action": "go_to", "params": {{"url": "https://example.com"}}}},
    {{"action": "click", "params": {{"selector": "#button"}}}},
    {{"action": "type", "params": {{"selector": "#input", "text": "value"}}}}
  ]
}}
"""
