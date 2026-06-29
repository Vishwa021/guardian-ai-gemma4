import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize Cerebras client
client = OpenAI(
    api_key=os.getenv("CEREBRAS_API_KEY"),
    base_url="https://api.cerebras.ai/v1"
)

# List available models
print("=" * 60)
print("Available Models:")
print("=" * 60)

models = client.models.list()

for model in models.data:
    print(f"• {model.id}")

print("\n" + "=" * 60)

# Test Gemma 4
response = client.chat.completions.create(
    model="gemma-4-31b",
    messages=[
        {
            "role": "system",
            "content": "You are Guardian AI, a cybersecurity expert."
        },
        {
            "role": "user",
            "content": "Introduce yourself in two lines."
        }
    ]
)

print("Gemma Response:\n")
print(response.choices[0].message.content)