"""
Cerebras API Client

Provides a single reusable client instance
for the entire Guardian AI application.
"""

from openai import OpenAI

from app.core.config import settings


class CerebrasClient:
    """Creates and manages the Cerebras API client."""

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.API_KEY,
            base_url=settings.BASE_URL
        )

    def get_client(self):
        """Return the initialized OpenAI client."""
        return self.client


# Global reusable instance
cerebras_client = CerebrasClient().get_client()