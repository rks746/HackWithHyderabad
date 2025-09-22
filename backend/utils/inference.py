import os
from ultralytics import YOLO

# Load your trained YOLOv8 model (weights inside models/)
MODEL_PATH = os.path.join("models", "yolov8_best.pt")
model = YOLO(MODEL_PATH)

def run_inference(image_path, save_folder="static"):
    """
    Run YOLO inference and save the annotated image
    """
    results = model.predict(source=image_path, save=True, save_dir=save_folder)

    # YOLO returns a list of results, we take the first
    result = results[0]
    predictions = []

    for box, conf, cls in zip(result.boxes.xyxy, result.boxes.conf, result.boxes.cls):
        predictions.append({
            "class_id": int(cls),
            "confidence": float(conf),
            "bbox": [float(x) for x in box]
        })

    # YOLO saves annotated image, we return the path
    annotated_image = os.path.join(save_folder, os.path.basename(image_path))
    return annotated_image, predictions
