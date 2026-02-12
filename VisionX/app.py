from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_image():
    file = request.files['image']
    operation = request.form['operation']

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    image = cv2.imread(filepath)

    if image is None:
        return "Image not loaded properly"

    if operation == "resize":
        image = cv2.resize(image, (300, 300))

    elif operation == "blur":
        image = cv2.GaussianBlur(image, (15, 15), 0)

    elif operation == "edge":
        image = cv2.Canny(image, 100, 200)

    elif operation == "rotate":
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    output_path = os.path.join(OUTPUT_FOLDER, "processed_" + file.filename)
    cv2.imwrite(output_path, image)

    return send_file(output_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
