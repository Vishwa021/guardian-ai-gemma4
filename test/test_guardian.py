from app.agents.coordinator import CoordinatorAgent
from app.models.request import AnalysisRequest

guardian = CoordinatorAgent()

request = AnalysisRequest(
    image_path="C:\\Users\\admin\\OneDrive\\Desktop\\Snip20170123_8.png",
    text="""
Your SBI account has been suspended.

Click below:

https://sbi-secure.xyz
"""
)

report = guardian.analyze(request)

print("\n========= AGENT REPORTS =========\n")

for agent in report.agent_reports:

    print(agent.agent_name)
    print(agent.status)
    print()

print("\n========= RISK =========\n")

print(report.risk_assessment.summary)

print("\n========= RECOMMENDATIONS =========\n")

print(report.recommendations.summary)