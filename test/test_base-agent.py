from app.agents.base_agent import BaseAgent


class TestAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Test Agent",
            system_prompt="You are a friendly assistant."
        )


agent = TestAgent()

response = agent.run("Say hello in one sentence.")

print(response)