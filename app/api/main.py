from fastapi import FastAPI
from app.services.guardian_service import GuardianService
from app.models.request import AnalysisRequest
from app.models.final_report import FinalReport
from fastapi import UploadFile, File, Form
from app.utils.file_manager import FileManager

app = FastAPI(
    title="Guardian AI",
    version="1.0.0"
)

guardian_service = GuardianService()

@app.get("/")
def root():
    return {
        "application": "Guardian AI",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post(
    "/analyze",
    response_model=FinalReport,
    summary="Analyze cybersecurity content"
)
def analyze(request: AnalysisRequest):

    return guardian_service.analyze(request)

@app.post("/analyze-upload")
async def analyze_upload(

    image: UploadFile = File(None),

    pdf: UploadFile = File(None),

    text: str = Form("")
):
    try:

        image_path = None
        pdf_path = None

        if image:
            image_path = FileManager.save_upload(image)

        if pdf:
            pdf_path = FileManager.save_upload(pdf)

        if image:

            image_path = FileManager.save_upload(image)

        request = AnalysisRequest(
    image_path=image_path,
    pdf_path=pdf_path,
    text=text
)
        return guardian_service.analyze(request)

    finally:

        if image_path:
            FileManager.delete_file(image_path)

        if pdf_path:
            FileManager.delete_file(pdf_path)