from pydantic import BaseModel
from typing import List, Optional, Union

class ActionParams(BaseModel):
    selector: Optional[str] = None
    text: Optional[str] = None
    url: Optional[str] = None
    modifiers: Optional[Union[str, List[str]]] = None

class Action(BaseModel):
    action: str
    params: ActionParams

class Plan(BaseModel):
    steps: List[Action]

class PlanRequest(BaseModel):
    command: str

class PlanResponse(BaseModel):
    steps: List[Action]

class ExecuteRequest(BaseModel):
    steps: List[Action]
