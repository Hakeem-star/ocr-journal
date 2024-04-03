from flask import Flask, json, jsonify, make_response, request
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

    @app.route("/generate-text", methods=["POST", "OPTIONS"])
    def generate_text():
        # Cors for local dev
        # print(request.form.get("file"))
        if request.method == "OPTIONS":  # CORS preflight
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.headers.add("Access-Control-Allow-Headers", "*")
            response.headers.add("Access-Control-Allow-Methods", "*")
            return response

        print(request.files)
        f: FileStorage = request.files["file"]
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

        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that provides a summary of text provided to you.",
                },
                {"role": "user", "content": text},
            ],
        )

        response = make_response(
            jsonify(
                {
                    "aiResponse": chat_response.choices[0].message.content
                    or "No summary generated",
                    "rawResponse": text,
                }
            )
        )

        # Cors for local dev
        response.headers.add("Access-Control-Allow-Origin", "*")

        return response
