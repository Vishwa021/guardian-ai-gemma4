from pydantic import BaseModel

from app.models.response import AgentResponse
from app.models.execution_summary import ExecutionSummary


class FinalReport(BaseModel):

    agent_reports: list[AgentResponse]

    risk_assessment: AgentResponse

    recommendations: AgentResponse

    execution_summary: ExecutionSummary