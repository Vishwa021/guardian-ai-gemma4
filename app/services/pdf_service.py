"""
PDF Text Extraction Service
"""

import fitz  # PyMuPDF


class PDFService:

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """
        Extract text from every page of a PDF.
        """

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text.strip()