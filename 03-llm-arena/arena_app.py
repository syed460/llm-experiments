# pip install openai gradio python-dotenv
import random
import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

openai_client = OpenAI()                                  # uses OPENAI_API_KEY
groq_client   = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
    )

def ask(client, model, prompt, temperature):
    r = client.chat.completions.create(
        model=model, 
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. "
                    "Answer naturally. Be creative when appropriate. "
                    "Avoid repeating common examples if possible."
                )
            },
            {"role": "user", "content": prompt}],
        temperature=temperature
        )
    return r.choices[0].message.content

def start_battle():
    return gr.Button("⏳ Battling...", interactive=False)

def battle(prompt, temperature):
    models = [
        ("GPT-4o Mini", openai_client, "gpt-4o-mini"),
        ("Llama 3.3 70B", groq_client, "llama-3.3-70b-versatile"),
    ]

    random.shuffle(models)

    model_a_name, client_a, model_a = models[0]
    model_b_name, client_b, model_b = models[1]

    answer_a = ask(client_a, model_a, prompt, temperature)
    answer_b = ask(client_b, model_b, prompt, temperature)

    return (
        answer_a,
        answer_b,
        model_a_name,
        model_b_name,
        gr.Button("⚔️ Battle!", interactive=True),
    )

def vote(vote_for, model_a, model_b):
    if vote_for == "A":
        winner = model_a
    else:
        winner = model_b

    return (
        f"🗳️ Thanks for voting!\n\n"
        f"🏆 You voted for **{winner}**."
    )

with gr.Blocks(title="LLM Arena") as demo:
    gr.Markdown("# 🥊 LLM Arena — one prompt, two models")
    prompt = gr.Textbox(label="Ask both models the same thing", lines=3)
    temperature = gr.Slider(
    minimum=0.0,
    maximum=2.0,
    value=0.7,
    step=0.1,
    label="Temperature",
    info="Lower = more consistent, Higher = more creative",
    )
    go = gr.Button("⚔️ Battle!", variant="primary")
    gr.Examples(
        examples=[
            ["Invent a completely new programming joke."],
            ["Explain quantum computing like I'm 10 years old."],
            ["What is the capital of France?"],
        ],
        inputs=prompt,
    )
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 🤖 Model A")
            out_a = gr.Markdown()
            with gr.Row():
                up_a   = gr.Button("👍");  down_a = gr.Button("👎")
        with gr.Column():
            gr.Markdown("### 🤖 Model B")
            out_b = gr.Markdown()
            with gr.Row():
                up_b   = gr.Button("👍");  down_b = gr.Button("👎")

    verdict = gr.Markdown()

    model_a_state = gr.State()
    model_b_state = gr.State()

    # go.click(
    #     battle,
    #     inputs=[prompt, temperature],
    #     outputs=[out_a, out_b, model_a_state, model_b_state]
    # )
    go.click(
        fn=start_battle,
        outputs=go,
    ).then(
        fn=battle,
        inputs=[prompt, temperature],
        outputs=[
            out_a,
            out_b,
            model_a_state,
            model_b_state,
            go,
        ],
    )

    up_a.click(
        lambda a, b: vote("A", a, b),
        inputs=[model_a_state, model_b_state],
        outputs=verdict,
    )

    down_a.click(
        lambda a, b: vote("A", a, b),
        inputs=[model_a_state, model_b_state],
        outputs=verdict,
    )

    up_b.click(
        lambda a, b: vote("B", a, b),
        inputs=[model_a_state, model_b_state],
        outputs=verdict,
    )

    down_b.click(
        lambda a, b: vote("B", a, b),
        inputs=[model_a_state, model_b_state],
        outputs=verdict,
    )

demo.launch(
    share=True,
    inbrowser=True,
    # debug=True,
    # show_error=True
    )