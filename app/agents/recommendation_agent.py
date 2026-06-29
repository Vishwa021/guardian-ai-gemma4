"""
Recommendation Agent

Generates practical cybersecurity recommendations
based on the overall risk assessment.
"""

from app.agents.base_agent import BaseAgent
from app.core.prompts import PromptLibrary
from app.models.response import AgentResponse


class RecommendationAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Recommendation Agent",
            system_prompt=PromptLibrary.RECOMMENDATION_AGENT
        )

    def generate_recommendations(
        self,
        risk_report: AgentResponse
    ) -> AgentResponse:
        """
        Generate recommendations from the Risk Agent's report.
        """

        return self.run(risk_report.summary)