# YOLOv8 Object Detection with Web Interface

![YOLOv8](https://user-images.githubusercontent.com/your-image-link.png)

## 🚀 Project Overview
This repository implements **YOLOv8** for object detection with a simple web interface built using Flask. Users can upload images, perform object detection, and view results directly in their browser.

## 🔥 Features
- 🏆 **State-of-the-art YOLOv8 model** for object detection.
- 🌐 **Web-based interface** for easy image uploads and visualization.
- ⚡ **Fast and efficient inference** on images and videos.
- 📈 **Supports fine-tuning on custom datasets**.
- 🛠️ **Pre-trained models available** for quick deployment.

## 📂 Folder Structure
```bash
├── data/                # Folder for storing input images
├── static/              # Static files (CSS, JS, etc.)
├── templates/           # HTML templates for the web app
├── yolo_env/            # Virtual environment folder
├── .gitignore           # Git ignore file
├── app.py               # Flask web application
├── best.pt              # Trained YOLOv8 model
├── README.md            # Project documentation
├── requirements.txt     # Required dependencies
```

## 🛠 Installation
Follow these steps to set up and run the project:

```bash
# Clone the repository
git clone https://github.com/ajaychaudhary2/Yolov8-Object-Detection.git
cd Yolov8-Object-Detection

# Create and activate a virtual environment
python -m venv yolo_env
source yolo_env/bin/activate  # On Windows use: yolo_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Running the Web App
```bash
python app.py
```
Then open your browser and go to `http://127.0.0.1:5000/` to use the web interface.

## 🚀 Quick Start (YOLOv8 Inference)
### 1️⃣ Run Object Detection on an Image
```bash
python scripts/inference.py --image path/to/image.jpg --model best.pt
```

### 2️⃣ Run Object Detection on a Video
```bash
python scripts/inference.py --video path/to/video.mp4 --model best.pt
```

## 📊 Results
YOLOv8 delivers impressive accuracy with real-time performance:
- 📌 **mAP@50**: 55-70% (depends on dataset)
- 🚀 **Inference Speed**: ~5-10ms per image on a modern GPU
- 🏆 **Supports multiple object categories**

## 📸 Sample Detections
| Input Image | Detection Output |
|-------------|-----------------|
| ![Input](https://user-images.githubusercontent.com/sample-input.jpg) | ![Output](https://user-images.githubusercontent.com/sample-output.jpg) |

## 📌 To-Do List
- [ ] Improve dataset support ✅
- [ ] Add real-time webcam detection 🎥
- [ ] Deploy as a web application 🌐
- [ ] Optimize for mobile devices 📱

## 🤝 Contributing
Contributions are always welcome! Feel free to fork the repository and submit a pull request.

## 📢 Connect with Me
- 🔗 **GitHub**: [@ajaychaudhary2](https://github.com/ajaychaudhary2)
- 💼 **LinkedIn**: https://www.linkedin.com/in/ajay-chaudhary-02287a2ab/
- ✉️ **Email**: ajaych2822@gmail.com

---

⭐ If you find this project helpful, don't forget to **star the repository** and follow for more exciting projects!

