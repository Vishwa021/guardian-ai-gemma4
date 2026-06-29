from app.core.cerebras_client import cerebras_client
from app.core.config import settings

response = cerebras_client.chat.completions.create(
    model=settings.MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

print(response.choices[0].message.content)