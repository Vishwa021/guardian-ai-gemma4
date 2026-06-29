from app.agents.coordinator import CoordinatorAgent
from app.models.request import AnalysisRequest

guardian = CoordinatorAgent()

request = AnalysisRequest(
    image_path="images/phishing.png",
    text="Check this email."
)
agents = guardian.select_agents(request)

print("\nSelected Agents:\n")

for agent in agents:
    print(agent.name)