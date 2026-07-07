# 🛍️ AI Shop Assistant

A simple AI shopping assistant built with **Python**, **OpenAI**, and **Gradio**.

The assistant can:

- 💬 Chat naturally with users
- 🧠 Remember previous conversation during the session
- 🛒 Use a function tool to look up product prices
- 🤖 Demonstrate OpenAI Function Calling (Tool Calling)

---

## 📸 Demo

<p align="center">
  <img src="demo/recording-2026-07-07-201425_BcqRvBAT.gif" alt="AI Shop Assistant Demo" width="900"/>
</p>

🎥 Full video: [demo/demo.mp4](demo/recording-2026-07-07-201425_BcqRvBAT.mp4)
---

## ✨ Features

- Chat interface built with Gradio
- OpenAI GPT-4o Mini
- Function Calling (Tool Calling)
- Conversation memory
- Product price lookup from a local JSON file
- Clean project structure

---

## 📁 Project Structure

```text
05-ai-shop-assistant/
│
├── app.py
├── agent.py
├── tools.py
├── constants.py
├── prices.json
├── requirements.txt
├── .env.example
├── README.md
└── demo/
    └── demo.gif
```

---

## ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/llm-experiments.git
```

Navigate to the project.

```bash
cd 05-ai-shop-assistant
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```powershell
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```text
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run

```bash
python app.py
```

Open:

```
http://127.0.0.1:7860
```

---

## 💬 Example Questions

- What can you help me with?
- How much are the shoes?
- What is the price of the bag?
- Compare the price of shoes and pants.
- My name is Syed.
- Do you remember my name?
- I work as a software engineer. What did I tell you earlier?

---

## 🛠️ Technologies Used

- Python
- OpenAI SDK
- GPT-4o Mini
- Gradio
- Python Dotenv

---

## 📚 Learning Objectives

This project demonstrates:

- OpenAI Chat Completions API
- Function Calling (Tool Calling)
- Conversation Memory
- Gradio Chat Interface
- Modular Python Project Structure

---

## 🚀 Future Improvements

- Multiple shopping tools
- Product search
- Product recommendations
- Shopping cart
- Persistent memory
- Database integration
- Order tracking