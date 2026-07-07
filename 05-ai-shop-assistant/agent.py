from tools import tools, get_price
from constants import MODEL, SYSTEM_PROMPT
import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()


def agent(user_message, history) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                SYSTEM_PROMPT
            )
        }
    ]

    print(f"history: {history}")  # ① Gradio fills this in for you


    """Example:
    history: [
    {'role': 'user', 'metadata': None, 'content': [{'text': 'hi chat', 'type': 'text'}], 'options': None}, 
    {'role': 'assistant', 'metadata': None, 'content': [{'text': 'Hello! How can I assist you today?', 'type': 'text'}], 'options': None}]
    """

    # for msg in history:
    #     messages.append(
    #         {
    #             "role": msg["role"],
    #             "content": msg["content"][0]["text"]
    #         }
    #     )
    messages.extend(history)

    # messages = [{"role": "user", "content": user_message}]
    messages.append({"role": "user", "content": user_message})

    print(f"messages: {messages}")  # ② messages is a global variable that persists across calls



    response = client.chat.completions.create(          # ① send message + tools menu
        model="gpt-4o-mini", 
        messages=messages, 
        tools=tools
        )
    
    msg = response.choices[0].message
    
    """Example:
    💬 model said: ChatCompletionMessage(
            content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, 
            tool_calls=[
                ChatCompletionMessageFunctionToolCall(
                id='call_aEyj7kUWKMfk3KwIG2jCkXGI', 
                function=Function(arguments='{"item":"shoes"}', 
                name='get_price'), 
                type='function')
            ])

    💬 model said: ChatCompletionMessage(
            content='Hello! I can assist you with a variety of tasks, including:...', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, 
            tool_calls=None)
    """

    if msg.tool_calls:                                  
        messages.append(msg)
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments)  

            result = get_price(args["item"]) # call the tool

            messages.append({"role": "tool", "tool_call_id": call.id, "content": result}) # pass tool result back to model

        response = client.chat.completions.create(      
            model=MODEL, 
            messages=messages
            )
        
        msg = response.choices[0].message

    return msg.content