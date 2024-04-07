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
            "content": prompt,
        },
            ]
    )
    print(response.choices[0])

    message = response.choices[0].message.content.strip()
    return message

