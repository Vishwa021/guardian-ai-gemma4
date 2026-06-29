"""
Image Service

Responsible for:
- Validating image files
- Encoding images to Base64
- Preparing image data for Gemma Vision
"""

import base64
from pathlib import Path


class ImageService:

    SUPPORTED_EXTENSIONS = {
        ".png",
        ".jpg",
        ".jpeg",
        ".webp"
    }

    @staticmethod
    def validate(image_path: str) -> bool:
        """
        Validate that the image exists and is supported.
        """

        path = Path(image_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        if path.suffix.lower() not in ImageService.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported image format: {path.suffix}"
            )

        return True

    @staticmethod
    def encode_base64(image_path: str) -> str:
        """
        Convert image into Base64 string.
        """

        ImageService.validate(image_path)

        with open(image_path, "rb") as image:
            encoded = base64.b64encode(image.read()).decode("utf-8")

        return encoded

    @staticmethod
    def mime_type(image_path: str) -> str:
        """
        Return MIME type from extension.
        """

        suffix = Path(image_path).suffix.lower()

        if suffix == ".png":
            return "image/png"

        if suffix == ".webp":
            return "image/webp"

        return "image/jpeg"