"""
Handles preprocessing of uploaded files before
they enter the AI pipeline.
"""

from app.models.request import AnalysisRequest
from app.services.pdf_service import PDFService


class FileProcessor:

    @staticmethod
    def process(request: AnalysisRequest) -> AnalysisRequest:
        """
        Prepare uploaded files for analysis.
        """

        # Process PDF
        if request.pdf_path:

            pdf_text = PDFService.extract_text(
                request.pdf_path
            )

            if request.text:
                request.text += "\n\n" + pdf_text
            else:
                request.text = pdf_text

        return request