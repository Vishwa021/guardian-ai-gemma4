from app.agents.coordinator import CoordinatorAgent
from app.models.request import AnalysisRequest

guardian = CoordinatorAgent()

request = AnalysisRequest(
    image_path="C:\\Users\\admin\\OneDrive\\Desktop\\Snip20170123_8.png",
    text="""
Your SBI account has been suspended.

Click here:
https://sbi-secure.xyz
"""
)

responses = guardian.execute_agents(request)

risk = guardian.run_risk_assessment(responses)

print(risk.summary)