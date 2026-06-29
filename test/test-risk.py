from app.models.response import AgentResponse
from app.agents.risk_agent import RiskAgent

vision = AgentResponse(
    agent_name="Vision Agent",
    status="SUCCESS",
    summary="Fake SBI login page requesting debit card details and OTP.",
    confidence=0.95,
    threat_detected=True,
    reasoning="Fake branding detected.",
    input_tokens=120,
    output_tokens=80,
    total_tokens=200,
    response_time=1.5
)

text = AgentResponse(
    agent_name="Text Agent",
    status="SUCCESS",
    summary="Email contains urgency and phishing language.",
    confidence=0.98,
    threat_detected=True,
    reasoning="Suspicious domain and urgency.",
    input_tokens=100,
    output_tokens=70,
    total_tokens=170,
    response_time=1.2
)

fraud = AgentResponse(
    agent_name="Fraud Agent",
    status="SUCCESS",
    summary="Credential harvesting attempt.",
    confidence=0.99,
    threat_detected=True,
    reasoning="OTP and CVV requested.",
    input_tokens=90,
    output_tokens=60,
    total_tokens=150,
    response_time=1.1
)

risk = RiskAgent()

response = risk.assess_risk([vision, text, fraud])

print(response.summary)

risk.display_metrics(response)