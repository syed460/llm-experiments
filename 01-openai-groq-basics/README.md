# 01 - OpenAI & Groq Basics

This project demonstrates how to interact with Large Language Models (LLMs) using the OpenAI Python SDK.

The same SDK can communicate with:
- OpenAI models
- Groq-hosted open-source models

## Objective

Learn how to:

- Configure API keys using environment variables
- Use the OpenAI Python SDK
- Send prompts to different LLM providers
- Compare how different providers are accessed

---

## Project Structure

```
01-openai-groq-basics/
│
├── groq_chat.py          # Groq Example
├── openai.py     # OpenAI Example
├── requirements.txt
├── .env.example
└── README.md
```

---

## Technologies

- Python
- OpenAI Python SDK
- Groq API
- python-dotenv

---

## Installation

Clone the repository.

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_openai_key

GROQ_API_KEY=your_groq_key
```

---

## Running OpenAI Example

```bash
python openai.py
```

Example prompt:

> Suggest one thing to do in Bangalore.

---

## Running Groq Example

```bash
python groq_chat.py
```

Example prompt:

> Tell me a joke.

---

## Key Learning

Although the models are hosted by different providers, the same OpenAI SDK can be used.

OpenAI

```python
client = OpenAI()
```

Groq

```python
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
```

Only the API key and `base_url` change.

---

## Concepts Learned

- LLM APIs
- Chat Completions API
- System Prompts
- User Prompts
- Environment Variables
- OpenAI SDK
- Groq Compatibility

---

## Future Improvements

- Streaming responses
- Model comparison
- Prompt engineering
- Function calling
- Website summarizer
