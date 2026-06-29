from app.agents.recommendation_agent import RecommendationAgent
from app.models.response import AgentResponse

risk = AgentResponse(
    agent_name="Risk Agent",
    status="SUCCESS",
    summary="""
Overall Risk: CRITICAL

Threat Summary:
A phishing campaign is attempting to steal
banking credentials and OTPs.

Immediate Actions:
Do not enter credentials.
""",
    confidence=0.99,
    threat_detected=True,
    reasoning="",
    input_tokens=150,
    output_tokens=100,
    total_tokens=250,
    response_time=2.1
)

agent = RecommendationAgent()

response = agent.generate_recommendations(risk)

print(response.summary)

agent.display_metrics(response)