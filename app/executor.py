# app/executor.py

from app.schemas import Plan
from playwright.sync_api import sync_playwright
import time

class Executor:
    def __init__(self):
        pass

    def execute_plan(self, plan: Plan):
        screenshots = []

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            for step in plan.steps:
                action = step.action
                params = step.params

                if action == "go_to" and params.url:
                    page.goto(params.url)
                    time.sleep(2)

                elif action == "click" and params.selector:
                    page.click(params.selector)
                    time.sleep(1)

                elif action == "type" and params.selector and params.text:
                    if params.modifiers:
                        page.keyboard.press(params.modifiers)
                    page.fill(params.selector, params.text)
                    time.sleep(1)

                else:
                    print(f"Unknown or incomplete action: {action}")

                screenshot = page.screenshot()
                screenshots.append(screenshot)

            browser.close()
        return screenshots
