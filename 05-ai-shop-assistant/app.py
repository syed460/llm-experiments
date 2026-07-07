import gradio as gr
from agent import agent          


def chat(message, history):      

    response = agent(message, history)

    return response


with gr.Blocks(theme=gr.themes.Soft(), title="🛍️ AI Shopping Assistant") as demo:

    gr.Markdown("""
    # 🛍️ AI Shopping Assistant
    Ask shopping questions naturally. The assistant can remember the conversation and use tools to look up product prices.
    """)

    gr.Markdown("""
    ### Available Products
    - 👟 Shoes, 🎩 Hat, 🩳 Shorts, 👖 Pants, 👜 Bag
    """)
    chatbot = gr.ChatInterface(
        fn=chat,
        title="",
        textbox=gr.Textbox(
            placeholder="Ask something like 'How much are the shoes?'",
            lines=2,
            submit_btn="🚀 Send",
        ),

    )

    gr.Examples(
        examples=[
        ["How much are the shoes?"],
        ["What is the price of the bag?"],
        ["Recommend a product under ₹1000."],
        ["My name is Mohamad."],
        ["I work as a software engineer."],
        ["Remember that I live in Bangalore."],
        ["Now ask me a question about myself."],
        ["What can you help me with?"],
        ],
        inputs=chatbot.textbox
    )

    gr.Markdown("""
    ---
    Built with ❤️ using **Python**, **OpenAI GPT-4o Mini**, **Function Calling**, and **Gradio**.
    """)

if __name__ == "__main__":
    demo.launch(
        theme=gr.themes.Soft(),
        # theme=gr.themes.Monochrome(),
        # theme=gr.themes.Glass(),
        # theme=gr.themes.Default(),
        
        share=True,
        inbrowser=True,
    )