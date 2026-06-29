from app.agents.coordinator import CoordinatorAgent
from app.models.request import AnalysisRequest

guardian = CoordinatorAgent()

request = AnalysisRequest(
    image_path="C:\\Users\\admin\\OneDrive\\Desktop\\Snip20170123_8.png",
    text="""
Dear Customer,

Your SBI account has been suspended.

Verify immediately:

https://sbi-secure.xyz
"""
)

responses = guardian.execute_agents(request)

risk = guardian.run_risk_assessment(responses)

recommendation = guardian.generate_recommendations(risk)

print("\n===== RISK =====\n")
print(risk.summary)

print("\n===== RECOMMENDATIONS =====\n")
print(recommendation.summary)