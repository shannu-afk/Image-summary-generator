from flask import Flask, render_template, request
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    image_path = ""
    if request.method == "POST":
        if "image" in request.files:
            image_file = request.files["image"]
            if image_file.filename != "":
                image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
                image_file.save(image_path)

                image = Image.open(image_path).convert("RGB")
                inputs = processor(images=image, return_tensors="pt")
                output = model.generate(**inputs)
                summary = processor.decode(output[0], skip_special_tokens=True)

    return render_template("index.html", summary=summary, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)