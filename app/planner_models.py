# app/planner_models.py

from pydantic import BaseModel
from typing import List, Dict

class ActionStep(BaseModel):
    action: str
    params: Dict

class ActionPlan(BaseModel):
    steps: List[ActionStep]
