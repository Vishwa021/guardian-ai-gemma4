from app.core.config import settings

print("API Key Loaded:", bool(settings.API_KEY))
print("Base URL:", settings.BASE_URL)
print("Model:", settings.MODEL_NAME)
print("Temperature:", settings.TEMPERATURE)
print("Max Tokens:", settings.MAX_TOKENS)
print("Debug:", settings.DEBUG)

#works