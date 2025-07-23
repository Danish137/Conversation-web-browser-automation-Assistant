# app/main.py

from fastapi import FastAPI
from app.schemas import PlanRequest, ExecuteRequest
from app.planner import Planner
from app.executor import Executor

app = FastAPI()
planner = Planner()
executor = Executor()

@app.post("/plan")
def generate_plan(request: PlanRequest):
    plan = planner.generate_plan(request.command)
    return plan

@app.post("/execute")
async def execute_plan(request: ExecuteRequest):
    screenshots = await executor.execute(request.steps)
    return {"message": "Execution completed", "screenshots": screenshots}
