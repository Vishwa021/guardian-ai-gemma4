from app.services.guardian_service import GuardianService
from app.models.request import AnalysisRequest

guardian = GuardianService()

request = AnalysisRequest(
    image_path="C:\\Users\\admin\\OneDrive\\Desktop\\Snip20170123_8.png",
    text="""
Your SBI account has been suspended.

Verify now:

https://sbi-secure.xyz
"""
)

report = guardian.analyze(request)

print(report.execution_summary)