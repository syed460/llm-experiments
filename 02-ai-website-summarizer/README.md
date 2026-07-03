# 🔎 AI Website Summarizer

An AI-powered web application that summarizes the content of any public website using an LLM.

Users simply provide a website URL, and the application:
1. Fetches the webpage content.
2. Extracts the readable text.
3. Sends the content to an LLM.
4. Returns a concise, well-formatted summary.

---

## 🚀 Demo

> Enter a website URL and click **🚀 Summarize**.

Example URLs:

- https://openai.com
- https://huggingface.co
- https://python.org

---

## 📸 Demo

<p align="center">
  <img src="demo/Recording 2026-07-03 105146.gif" alt="AI Website Summarizer Demo" width="900"/>
</p>

---

## 🏗️ Project Structure

```
02-ai-website-summarizer/
│
├── app.py
├── scraper.py
├── summarizer.py
├── requirements.txt
├── .env.example
├── README.md
└── screenshots/
```

---

## 🛠️ Technologies Used

- Python
- OpenAI Python SDK
- Gradio
- BeautifulSoup
- Requests
- python-dotenv

---

## ⚙️ How It Works

```
Website URL
      │
      ▼
Fetch HTML
      │
      ▼
Extract Readable Text
      │
      ▼
Create Prompt
      │
      ▼
GPT-4o Mini
      │
      ▼
Markdown Summary
      │
      ▼
Gradio UI
```

---

## 📦 Installation

Clone the repository.

```bash
git clone <repository-url>
cd 02-ai-website-summarizer
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

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser.

```
http://127.0.0.1:7860
```

---

## 🧠 Learning Outcomes

Through this project I learned:

- Calling an LLM using the OpenAI Python SDK
- Prompt Engineering using System and User prompts
- Web scraping using BeautifulSoup
- Cleaning webpage content before sending it to the model
- Building a simple AI application using Gradio
- Managing API keys using environment variables

---

## 📚 Key Components

### scraper.py

Responsible for:

- Downloading the webpage
- Removing unnecessary HTML elements
- Extracting readable text

---

### summarizer.py

Responsible for:

- Creating the prompt
- Calling the GPT-4o Mini model
- Returning the generated summary

---

### app.py

Responsible for:

- Creating the Gradio interface
- Accepting website URLs
- Displaying the generated summary

---

## 💡 Future Improvements

- Support Groq-hosted models
- Compare summaries from multiple LLMs
- Streaming responses
- Copy summary button
- Download summary as Markdown
- PDF export
- URL validation
- Dark mode
- Deploy to Hugging Face Spaces

---

## 📄 License

This project is created for learning purposes as part of my AI Engineering journey.