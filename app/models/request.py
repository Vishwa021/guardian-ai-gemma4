from pydantic import BaseModel


class UserRequest(BaseModel):
    """
    Represents a request sent by the frontend.
    """

    user_input: str
    image_path: str | None = None
    pdf_path: str | None = None