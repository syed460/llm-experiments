# 🥊 LLM Arena

An AI application that sends the same prompt to two different Large Language Models (LLMs) and displays their responses side by side for comparison.

> **Inspired by AI model arenas where users compare responses from multiple LLMs and vote for the better answer.**

---

## 🚀 Features

- 🤖 Compare responses from GPT-4o Mini and Llama 3.3 70B
- ⚔️ Send the same prompt to both models simultaneously
- 🌡️ Adjust the temperature to control creativity
- 👍 Vote for your preferred response
- 🎲 Anonymous Model A / Model B comparison
- 🏆 Reveal the model names after voting
- 💡 Built-in example prompts
- 🎨 Interactive Gradio interface
- 🔐 Secure API key management using `.env`

---

## 📸 Demo

<p align="center">
  <img src="demo/Recording 2026-07-05 154457.gif" alt="LLM Arena Demo" width="900"/>
</p>

<p align="center">
  <em>Compare responses from GPT-4o Mini and Llama 3.3 side by side, then vote for the better answer.</em>
</p>

---

## 🏗️ Project Structure

```
03-llm-arena/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── demo/
```

---

## 🛠️ Technologies Used

- Python
- OpenAI Python SDK
- OpenAI GPT-4o Mini
- Groq API
- Llama 3.3 70B Versatile
- Gradio
- python-dotenv

---

## ⚙️ How It Works

```
                 User Prompt
                      │
                      ▼
            Select Temperature
                      │
                      ▼
        ┌─────────────────────────┐
        │ Same Prompt Sent to Both│
        └─────────────────────────┘
              │              │
              ▼              ▼
         GPT-4o Mini    Llama 3.3 70B
              │              │
              ▼              ▼
          Model A        Model B
              │              │
              └──────┬───────┘
                     ▼
            User Compares Answers
                     ▼
               User Casts Vote
                     ▼
         Reveal Actual Model Names
```

---

## 📦 Installation

Clone the repository.

```bash
git clone <repository-url>
cd 03-llm-arena
```

Create a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_api_key

GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open the browser.

```
http://127.0.0.1:7860
```

---

## 🧪 Example Prompt

```
Explain quantum computing in simple words.
```

or

```
Write a Python function to reverse a linked list.
```

or

```
Plan a 3-day trip to Bangalore.
```

---

## 🧠 Learning Outcomes

Through this project I learned:

- Calling multiple LLM providers using the OpenAI SDK
- Integrating OpenAI and Groq in one application
- Comparing responses from different LLMs
- Using temperature to control model creativity
- Building interactive Gradio applications
- Managing application state with Gradio
- Prompt engineering
- Secure API key management using `.env`

---

## 🔍 Models Used

| Provider | Model |
|----------|-------|
| OpenAI | GPT-4o Mini |
| Groq | Llama 3.3 70B Versatile |

---

## 📚 Key Components

### app.py

Responsible for:

- Sending the same prompt to two different LLMs
- Displaying responses side by side
- Collecting user votes
- Building the Gradio interface

---

## 💡 Future Improvements

- Store voting history in a database
- Display response latency
- Compare token usage and cost
- Support additional models (Claude, Gemini, DeepSeek, Qwen)
- Allow custom system prompts
- Stream responses as they're generated
- Deploy to Hugging Face Spaces
- Add leaderboard and voting statistics

---

## 📄 License

This project was built for learning purposes as part of my AI Engineering journey.