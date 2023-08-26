import chainlit as cl
import openai

@cl.on_message
async def main(message: str):
    await cl.Message(content = message).send()