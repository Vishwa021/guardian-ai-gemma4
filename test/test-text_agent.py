from app.agents.text_agent import TextAgent

agent = TextAgent()

response = agent.analyze_text("""
Subject: Urgent Account Verification

Dear Customer,

Your SBI account has been suspended.

Please verify immediately by clicking:

https://sbi-secure-login.xyz

Failure to verify within 30 minutes will permanently suspend your account.

Regards,
SBI Team
""")

print(response)