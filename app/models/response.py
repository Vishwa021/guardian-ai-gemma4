from pydantic import BaseModel


class AgentResponse(BaseModel):
    """
    Standard response returned by every AI agent.
    """

    agent_name: str
    status: str          # SUCCESS / FAILED
    summary: str
    confidence: float
    threat_detected: bool
    reasoning: str