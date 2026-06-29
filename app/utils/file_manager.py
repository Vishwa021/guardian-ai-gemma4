"""
Handles uploaded files.
"""

import shutil
import uuid
from pathlib import Path

UPLOAD_FOLDER = Path("uploads")

UPLOAD_FOLDER.mkdir(exist_ok=True)


class FileManager:

    @staticmethod
    def save_upload(upload_file):

        extension = Path(upload_file.filename).suffix

        filename = f"{uuid.uuid4()}{extension}"

        filepath = UPLOAD_FOLDER / filename

        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

        return str(filepath)

    @staticmethod
    def delete_file(filepath):

        path = Path(filepath)

        if path.exists():
            path.unlink()