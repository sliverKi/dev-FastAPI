import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
client = OpenAI(api_key = OPENAI_KEY)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{
        'role':'system',
        'content':'You are a helpful assistant'
    }]
)
print(response.choices[0].message.content)