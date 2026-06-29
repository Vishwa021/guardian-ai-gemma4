from app.models.request import AnalysisRequest
from app.services.file_processor import FileProcessor

request = AnalysisRequest(
    pdf_path="sample-pdf-tiny.pdf"
)

processed = FileProcessor.process(request)

print(processed.text[:500])