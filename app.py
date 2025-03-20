from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# Paths
BASE_DIR = r"E:\Data_Science _master\DL\CNN\Object detection\Yolo8\ObjectDetection_webapp_yolov8"
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
PROCESSED_FOLDER = os.path.join(BASE_DIR, "static", "Prediction")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PROCESSED_FOLDER"] = PROCESSED_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# Load YOLO model
model_path = os.path.join(BASE_DIR, "best.pt")
model = YOLO(model_path)

@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            # Save uploaded image
            img_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(img_path)

            # Run YOLO detection
            results = model(img_path)
            result = results[0]

            # Read the image
            img = cv2.imread(img_path)

            # Draw bounding boxes with class names and confidence scores
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                conf = float(box.conf[0])  # Confidence score
                cls = int(box.cls[0])  # Class index
                
                # Get class name
                class_name = model.names[cls] if hasattr(model, 'names') else f"Class {cls}"
                
                # Draw bounding box
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Put text with class name & confidence score
                label = f"{class_name}: {conf:.2f}"
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Save processed image
            processed_path = os.path.join(app.config["PROCESSED_FOLDER"], file.filename)
            success = cv2.imwrite(processed_path, img)

            if not success:
                print(f"❌ Error: Processed image was not saved at {processed_path}")
                return render_template("index.html", uploaded_img=None, processed_img=None)

            # Convert to relative paths for HTML display
            uploaded_img_url = url_for("static", filename=f"uploads/{file.filename}")
            processed_img_url = url_for("serve_prediction", filename=file.filename)

            return render_template("index.html", uploaded_img=uploaded_img_url, processed_img=processed_img_url)

    return render_template("index.html", uploaded_img=None, processed_img=None)

# Serve processed images correctly
@app.route("/static/Prediction/<filename>")
def serve_prediction(filename):
    return send_from_directory(app.config["PROCESSED_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
