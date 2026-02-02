# 🎯 YOLOv8 Real-Time Video Object Detection

This project performs object detection on video files using the YOLOv8 deep learning model. It identifies multiple objects in each frame and produces a new video with bounding boxes, labels, and confidence scores.

---

## 📌 Table of Contents

- [About This Project](#about-this-project)
- [What This System Can Do](#what-this-system-can-do)
- [Tools & Libraries Used](#tools--libraries-used)
- [How The Detection Works](#how-the-detection-works)
- [Installation Guide](#installation-guide)
- [How To Run The Detection](#how-to-run-the-detection)
- [Understanding The Output](#understanding-the-output)
- [Making It Run Faster](#making-it-run-faster)
- [Project File Structure](#project-file-structure)
- [What Can Be Improved](#what-can-be-improved)
- [License](#license)

---

## 🧠 About This Project

This system uses **YOLOv8** (You Only Look Once) to detect objects in video footage.  
The model processes each frame of a video, identifies objects like people, cars, animals, and more, and then saves a new annotated video showing those detections.

This project was tested using a **[mention: GPU / CPU / Google Colab / Local PC]**.

---

## 🚀 What This System Can Do

✔ Detect multiple objects in a video  
✔ Draw bounding boxes around detected objects  
✔ Show object names and confidence scores  
✔ Save a new video with all detections visualized  
✔ Use GPU acceleration for faster performance  
✔ Process long videos by splitting them into smaller clips  

---

## 🛠 Tools & Libraries Used

- Python 3.x  
- Ultralytics YOLOv8  
- OpenCV  
- FFmpeg (for cutting long videos)  
- [Optional: Google Colab / NVIDIA GPU]

---

## ⚙️ How The Detection Works

1. A pre-trained YOLOv8 model is loaded (`yolov8n.pt`)
2. The system reads a video file frame by frame
3. YOLO detects objects and returns:
   - Object class (person, car, etc.)
   - Bounding box coordinates
   - Confidence score
4. The frame is annotated with boxes and labels
5. A new output video is generated with these detections

---

## 💻 Installation Guide

Install required libraries:

```bash```
pip install  ultralytics  opencv-python 

If using long videos, install FFmpeg:

Linux: sudo apt install ffmpeg

Windows/Mac: Download from https://ffmpeg.org/

## ▶️ How To Run The Detection

Place your video in the project folder and rename it:

test.mp4


Run this Python script:

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.predict(
    source="test.mp4",
    save=True,
    imgsz=640,
    conf=0.25,
    device="0"  # Use "cpu" if no GPU
)

## 🎬 Understanding The Output

After processing finishes, YOLO creates a new video here:

runs/detect/predict/test.mp4


This output video shows:

Bounding boxes around objects

Object labels (person, car, dog, etc.)

Confidence scores

## ⚡ Making It Run Faster

If detection is slow:

Use GPU instead of CPU

Use yolov8n.pt (fastest model)

Reduce frame size using imgsz=640

Split long videos into smaller clips before processing

## 📁 Project File Structure
project-folder/
│
├── test.mp4      # Original video

├── detection_script.py # YOLO detection code

├── README.md    # Project documentation

└── runs/
    └── detect/
        └── predict/       # Output videos

## 🔮 What Can Be Improved

Add live FPS counter on output video

Detect only specific object classes

Save detection results to CSV file

Build a web interface for uploads

Real-time alerts for specific objects

## 📄 License

This project is for educational purposes. You may modify and use it freely.
