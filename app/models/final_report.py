from pydantic import BaseModel

from app.models.response import AgentResponse


class FinalReport(BaseModel):
    """
    Complete report returned by Guardian AI.
    """

    agent_reports: list[AgentResponse]

    risk_assessment: AgentResponse

    recommendations: AgentResponse