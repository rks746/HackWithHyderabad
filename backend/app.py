import os
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from utils.inference import run_inference   

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "static"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Run inference
        result_path, predictions = run_inference(filepath, app.config["RESULT_FOLDER"])

        return jsonify({
            "predictions": predictions,
            "result_image": result_path
        })

    return jsonify({"error": "File type not allowed"}), 400

@app.route("/static/<filename>")
def get_result(filename):
    return send_from_directory(app.config["RESULT_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
