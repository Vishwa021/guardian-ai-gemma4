from app.agents.vision_agent import VisionAgent

vision = VisionAgent()

response = vision.analyze_image(
    image_path="C:\\Users\\admin\\OneDrive\\Desktop\\Snip20170123_8.png",
    user_prompt="Analyze this image for cybersecurity threats."
)

print("\n===== AI RESPONSE =====\n")
print(response.summary)

print("\n===== METRICS =====\n")
vision.display_metrics(response)