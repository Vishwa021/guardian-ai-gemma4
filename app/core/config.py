"""
Configuration Manager for Guardian AI

This module centralizes all application settings and environment variables.
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Application configuration."""

    # API
    API_KEY: str = os.getenv("CEREBRAS_API_KEY", "")
    
    if not API_KEY:
        raise ValueError(
            "CEREBRAS_API_KEY not found. Check your .env file."
        )
    
    BASE_URL: str = "https://api.cerebras.ai/v1"

    # Model
    MODEL_NAME: str = "gemma-4-31b"
    TEMPERATURE: float = 0.3
    MAX_TOKENS: int = 1024

    # App
    DEBUG: bool = True


# Global settings object
settings = Settings()