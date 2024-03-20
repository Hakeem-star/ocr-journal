from flask import Flask, request
from werkzeug.datastructures import FileStorage
import pytesseract
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def ai_actions(app: Flask):

    @app.post("/generate-text")
    def generate_text():
        f: FileStorage = request.files["image"]
        print(f.filename)
        image_file = "./assets/testocr_1.png"
        f.save(image_file)

        pytesseract.pytesseract.tesseract_cmd = (
            "C:/Program Files/Tesseract-OCR/tesseract.exe"
        )

        text = pytesseract.image_to_string(image_file)
        print(text)

        summary = get_ai_summary(client, text)
        return summary

    def get_ai_summary(client: OpenAI, text: str):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that provides a summary of text provided to you.",
                },
                {"role": "user", "content": text},
            ],
        )

        return response.choices[0].message.content or "No summary generated"
