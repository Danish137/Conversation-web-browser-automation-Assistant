# test_planner.py

from app.planner import Planner
from app.schemas import Plan

def main():
    planner = Planner()

    user_input = "Send a leave email to imdanishakhtar137@gmail.com with the subject 'Leave Request' and message 'I need leave from 15th to 20th July.'"

    try:
        plan: Plan = planner.generate_plan(user_input)
        print("✅ Generated Plan:")
        print(plan.model_dump_json(indent=2))  # Updated from plan.json()
    except Exception as e:
        print(f"❌ Planner failed: {e}")

if __name__ == "__main__":
    main()
