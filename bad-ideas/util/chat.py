import openai
import os

openai.my_api_key = os.environ["GPTKEY"]
print(os.environ["GPTKEY"])

messages = [{"role": "system", "content": "You are a intelligent assistant."}]

def do_chat(text):

    messages.append(
        {"role": "user", "content": text},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})