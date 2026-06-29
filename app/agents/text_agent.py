"""
Text Agent

Responsible for analyzing text-based
cybersecurity threats.
"""

from app.agents.base_agent import BaseAgent
from app.core.prompts import PromptLibrary


class TextAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Text Agent",
            system_prompt=PromptLibrary.TEXT_AGENT
        )

    def analyze_text(self, text: str) -> str:
        """
        Analyze suspicious text.
        """
        return self.run(text)