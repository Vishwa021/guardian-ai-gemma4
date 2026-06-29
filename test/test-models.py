from app.models.request import UserRequest
from app.models.response import AgentResponse
from app.models.report import SecurityReport

request = UserRequest(
    user_input="I received this suspicious email."
)

print(request)

response = AgentResponse(
    agent_name="Text Agent",
    summary="Possible phishing email.",
    confidence=93.5,
    threat_detected=True
)

print(response)

report = SecurityReport(
    overall_risk="High",
    confidence=94.2,
    findings=[
        "Suspicious sender",
        "Credential harvesting attempt"
    ],
    recommendations=[
        "Do not click links.",
        "Report the sender."
    ]
)

print(report)