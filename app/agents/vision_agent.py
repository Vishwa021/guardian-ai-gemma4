"""
Vision Agent

Analyzes images using Gemma 4 Vision.
"""

from app.agents.base_agent import BaseAgent
from app.core.prompts import PromptLibrary
from app.services.image_service import ImageService


class VisionAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Vision Agent",
            system_prompt=PromptLibrary.VISION_AGENT
        )

    def analyze_image(
        self,
        image_path: str,
        user_prompt: str = "Analyze this image for cybersecurity threats."
    ) -> str:

        image_base64 = ImageService.encode_base64(image_path)

        mime = ImageService.mime_type(image_path)

        messages = [
        {
        "role": "system",
        "content": self.system_prompt
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mime};base64,{image_base64}"
                    }
                }
            ]
        }
        ]

        return self._send_request(messages)