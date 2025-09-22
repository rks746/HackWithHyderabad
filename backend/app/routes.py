from flask import Blueprint, request, jsonify, send_from_directory, current_app
from PIL import Image, ImageDraw
import os
import uuid


api_bp = Blueprint("api", __name__)


@api_bp.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = f"{uuid.uuid4().hex}_{file.filename}"
    upload_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    annotated_path = os.path.join(current_app.config["ANNOTATED_FOLDER"], filename)
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)
    os.makedirs(os.path.dirname(annotated_path), exist_ok=True)
    file.save(upload_path)

    # Mock: open image and draw a sample bounding box
    image = Image.open(upload_path).convert("RGB")
    draw = ImageDraw.Draw(image)
    width, height = image.size
    box = [int(width * 0.1), int(height * 0.1), int(width * 0.6), int(height * 0.6)]
    draw.rectangle(box, outline="red", width=4)
    image.save(annotated_path)

    response = {
        "boxes": [
            {
                "x1": box[0],
                "y1": box[1],
                "x2": box[2],
                "y2": box[3],
                "label": "mock_object",
                "confidence": 0.85,
            }
        ],
        "annotated_image_url": f"/annotated/{filename}",
    }
    return jsonify(response), 200


@api_bp.route("/annotated/<path:filename>", methods=["GET"])
def get_annotated(filename: str):
    return send_from_directory(current_app.config["ANNOTATED_FOLDER"], filename)


@api_bp.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json(silent=True) or {}
    note = data.get("note")
    if not note:
        return jsonify({"error": "Missing note"}), 400
    feedback_id = uuid.uuid4().hex
    # Mock: in the future, persist feedback to DB or file
    return jsonify({"status": "received", "feedback_id": feedback_id}), 200


