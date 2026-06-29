"""
Fraud Agent

Specialized AI agent for detecting
financial fraud and scams.
"""

from app.agents.base_agent import BaseAgent
from app.core.prompts import PromptLibrary


class FraudAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Fraud Agent",
            system_prompt=PromptLibrary.FRAUD_AGENT
        )

    def analyze_fraud(self, text: str) -> str:
        """
        Analyze financial fraud attempts.
        """
        return self.run(text)