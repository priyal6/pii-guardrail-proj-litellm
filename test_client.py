from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="http://localhost:4000"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            'role': 'user',
            'content':  'Repeat back my exact words: My name is John Smith, my email is john.smith@gmail.com, and my card is 4111-1111-1111-1111.'

        }
    ],
    extra_body={
        "guardrails": ["presidio-pii-guard"]
    }
)

print(response.choices[0].message.content)