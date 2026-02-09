
pip install ultralytics opencv-python

!pip install ultralytics --upgrade

from ultralytics import YOLO

print("Ultralytics YOLO is installed and ready!")

from ultralytics import YOLO

# 1️⃣ Load YOLOv8 model
# Nano = fastest. Switch to yolov8s.pt for higher accuracy
model = YOLO("yolov8n.pt")

# 2️⃣ Video input path
video_path = "test.mp4"  # Replace with your video file

# 3️⃣ Run YOLO detection
# Optimized for GPU and speed
results = model.predict(
    source=video_path,   # Input video
    save=True,           # Save output video automatically
    imgsz=640,           # Resize frames (speed boost)
    conf=0.25,           # Minimum confidence threshold
    device="0",          # GPU device (0 = first GPU)
    show=False           # Do not open GUI windows
)

# 4️⃣ Print summary per frame
print("\n🚀 Detection complete!")
print(f"✅ Output saved in folder: {results[0].path}")  # Output video path

# Optional: print all detected objects per frame
for frame_idx, frame_result in enumerate(results):
    boxes = frame_result.boxes
    print(f"\n📸 Frame {frame_idx + 1}: {len(boxes)} objects detected")
    for box in boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        print(f" - {label} ({conf:.2f}) at [{x1}, {y1}, {x2}, {y2}]")

print("\n🎬 All done! Open the video in 'runs/detect/' to see detections visually.")

from google.colab import files

files.download('runs/detect/predict/test.avi')
