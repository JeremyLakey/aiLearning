import openai
from openai import OpenAI
import os


def do_chat(prompt, model="gpt-3.5-turbo"):
    client = OpenAI(api_key = os.environ["GPTKEY"])

    response = client.chat.completions.create(
        model=model,
        messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
            ]
    )

    message = response.choices[0].text.strip()
    return message

