# 🧠 Conversational Web-Browser Automation Assistant

An AI-powered assistant that can understand natural language commands and automate real browser tasks like sending emails, navigating pages, and performing actions — all through conversation.

## 🚀 Features

- 🧑‍💻 **Conversational Interface** via Streamlit
- 🌐 **Real-Time Browser Automation** using Playwright
- 🤖 **Natural Language Command Parsing**
- 📋 **Plan & Execute Architecture**:
  - LLM generates a step-by-step plan from user instructions
  - Each step is executed live on a browser instance
- 📷 **Live Screenshot Feedback** of browser actions
- 🧠 **Context Memory** to retain conversational history
- 🔐 **Secure Gmail Login** using App Passwords (no 2FA/captcha issues)

## 🛠 Tech Stack

| Layer            | Tool / Library           |
|------------------|--------------------------|
| Backend API      | FastAPI                  |
| Frontend         | Streamlit                |
| Browser Control  | Playwright               |
| LLM Integration  | OpenRouter / Groq / OpenAI (configurable) |
| Memory & Cache   | LangChain + Redis (optional) |
| TTS (Optional)   | ElevenLabs               |

## 🗂️ Project Structure

📁 app/
├── main.py # FastAPI app
├── planner.py # Plan generation from LLM
├── executor.py # Executes each step in browser
├── utils.py # Helper functions
├── schemas.py # Pydantic models
📁 ui/
└── streamlit_app.py # Chat interface
.env # Environment secrets
requirements.txt


## 🧪 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/Danish137/Conversation-web-browser-automation-Assistant.git
cd Conversation-web-browser-automation-Assistant


