from app.executor import Executor
from app.config import Config

config = Config()
executor = Executor(config)

sample_plan = [
    {"type": "go_to", "url": "https://example.com"},
    {"type": "wait_for", "selector": "h1"},
    {"type": "click", "selector": "h1"}  # Example, may fail gracefully
]

result = executor.execute_plan(sample_plan)

print("Execution Result:")
for step in result:
    print(step)
