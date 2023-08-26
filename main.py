import chainlit as cl
from openai import ChatCompletion

@cl.on_message
async def main(message: str):
    
    response = ChatCompletion.create(
        model = 'gpt-4',
        messages = [
            {"role": "assistant", "content": "you are an assistant that think like Nietzsche"},
            {"role": "user", "content": message}
        ],
        
        temperature = 1,
    )
    
    await cl.Message(content = f"{response['choices'][0]['message']['content']}", ).send()