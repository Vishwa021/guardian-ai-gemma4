from pydantic import BaseModel


class AgentResponse(BaseModel):
    """
    Standard response returned by every AI agent.
    """

    agent_name: str

    status: str

    summary: str

    confidence: float = 0.0

    threat_detected: bool = False

    reasoning: str = ""

    input_tokens: int

    output_tokens: int

    total_tokens: int

    response_time: float