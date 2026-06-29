import requests


BASE_URL = "https://guardian-ai-gemma4.onrender.com"


class APIClient:

    @staticmethod
    def analyze(image=None, pdf=None, text=""):

        files = {}
        data = {"text": text}

        if image:
            files["image"] = (
                image.name,
                image,
                image.type
            )

        if pdf:
            files["pdf"] = (
                pdf.name,
                pdf,
                pdf.type
            )

        response = requests.post(
            f"{BASE_URL}/analyze-upload",
            files=files,
            data=data
        )

        response.raise_for_status()

        return response.json()