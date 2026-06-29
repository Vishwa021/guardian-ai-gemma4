from pathlib import Path

ALLOWED_IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp"
}

ALLOWED_DOCUMENT_EXTENSIONS = {
    ".pdf"
}


def is_valid_image(path: str) -> bool:
    return Path(path).suffix.lower() in ALLOWED_IMAGE_EXTENSIONS


def is_valid_document(path: str) -> bool:
    return Path(path).suffix.lower() in ALLOWED_DOCUMENT_EXTENSIONS