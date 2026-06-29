from app.agents.vision_agent import VisionAgent

vision = VisionAgent()

response = vision.analyze_image(
    image_path="C:\\Users\\admin\\OneDrive\\Desktop\\Snip20170123_8.png",
    user_prompt="""
You are a cybersecurity analyst.

Analyze this image.

Check for:

- Phishing
- Scam
- Fake branding
- Credential theft
- Fake login page

Return:

Threat Level:
Reason:
Recommendation:
"""
)

print(response)