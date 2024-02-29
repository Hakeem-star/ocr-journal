from flask import Flask, request
from werkzeug.datastructures import FileStorage
import pytesseract


app = Flask(__name__)


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

    return "Thank you come again!"


# $ curl -F "image=@./assets/testocr.png" http://127.0.0.1:5000/generate-text
