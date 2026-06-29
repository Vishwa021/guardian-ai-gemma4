from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    """
    Represents a user request to Guardian AI.
    """

    image_path: str | None = None

    text: str | None = None

    pdf_path: str | None = None
