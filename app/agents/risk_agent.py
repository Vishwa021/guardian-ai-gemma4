"""
Risk Assessment Agent

Responsible for evaluating the overall
risk based on reports from other agents.
"""

from app.agents.base_agent import BaseAgent
from app.core.prompts import PromptLibrary
from app.utils.report_builder import ReportBuilder
from app.models.response import AgentResponse


class RiskAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Risk Agent",
            system_prompt=PromptLibrary.RISK_AGENT
        )

    def assess_risk(self, reports: list[AgentResponse]) -> AgentResponse:
        """
        Assess overall cybersecurity risk using
        reports from other agents.
        """

        combined_report = ReportBuilder.combine(reports)

        return self.run(combined_report)