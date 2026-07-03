# pip install gradio
import gradio as gr
from summarizer import summarize

demo = gr.Interface(
    fn=summarize,
    examples=[
        ["https://openai.com"],
        ["https://huggingface.co"],
        ["https://python.org"],
    ],
    inputs=gr.Textbox(
        label="Website URL",
        placeholder="https://example.com",
        lines=1,
    ),
    outputs=gr.Markdown(label="Summary"),
    title="🔎 AI Website Summarizer",
    description="Summarize any webpage using an LLM.",
    submit_btn="🚀 Summarize",
)

if __name__ == "__main__":
    demo.launch(
        share=True,
        inbrowser=True
    )

