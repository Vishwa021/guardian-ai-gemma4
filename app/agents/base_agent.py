"""
Base Agent for Guardian AI

Every AI agent inherits from this class.
"""

from abc import ABC
from tracemalloc import start
from urllib import response
from app.core.cerebras_client import cerebras_client
from app.core.config import settings
import time
from app.models.response import AgentResponse


class BaseAgent(ABC):
    """
    Base class for all Guardian AI agents.
    """

    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.client = cerebras_client
        self.model = settings.MODEL_NAME
    
    def display_metrics(self, response: AgentResponse):

        print("\n" + "=" * 60)
        print(f"Agent          : {response.agent_name}")
        print(f"Status         : {response.status}")
        print(f"Response Time  : {response.response_time:.2f} sec")
        print(f"Input Tokens   : {response.input_tokens}")
        print(f"Output Tokens  : {response.output_tokens}")
        print(f"Total Tokens   : {response.total_tokens}")
        print("=" * 60)

    def _send_request(self, messages) -> AgentResponse:
        """
        Send a request to the LLM and return a standardized AgentResponse.
        """

        start = time.perf_counter()

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )

            end = time.perf_counter()

            return AgentResponse(
                agent_name=self.name,
                status="SUCCESS",
                summary=response.choices[0].message.content,
                confidence=0.0,
                threat_detected=False,
                reasoning="",
                input_tokens=response.usage.prompt_tokens,
                output_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
                response_time=round(end - start, 2)
            )

        except Exception as e:

            end = time.perf_counter()

            return AgentResponse(
                agent_name=self.name,
                status="FAILED",
                summary="",
                confidence=0.0,
                threat_detected=False,
                reasoning=str(e),
                input_tokens=0,
                output_tokens=0,
                total_tokens=0,
                response_time=round(end - start, 2)
            )
    
    def run(self, user_input: str) -> AgentResponse:

        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ]

        return self._send_request(messages)