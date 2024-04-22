from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Define multiple chat requests
requests = [
    {
        "role": "system",
        "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
    },
    {
        "role": "user",
        "content": "Compose a poem that explains the concept of recursion in programming."
    },
    # Add more requests here if needed
]

# Send multiple chat requests in a single API call
completions = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=requests
)

# Process and print individual completions
for completion in completions.choices:
    print(completion.message.content)
