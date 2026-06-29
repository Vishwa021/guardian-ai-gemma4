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

responses = guardian.execute_agents(request)

print("\nExecuted Agents:\n")

for response in responses:

    print("=" * 60)

    print(response.agent_name)

    print(response.status)

    print(response.response_time)

    print(response.total_tokens)

    print("=" * 60)