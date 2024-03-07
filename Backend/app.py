from flask import Flask, request
from werkzeug.datastructures import FileStorage
import pytesseract
from openai import OpenAI
import os
from dotenv import load_dotenv

from utils.gpt import get_ai_summary

load_dotenv()
app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


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


# $ curl -F "image=@./assets/testocr.png" http://127.0.0.1:5000/generate-text
