from ultralytics import YOLO

# Load a model
# model = YOLO('yolov8n.pt')  # load an official detection model
# model = YOLO('yolov8n-seg.pt')  # load an official segmentation model
model = YOLO('runs/detect/train5/weights/best.pt')  # load a custom model

# Track with the model
results = model.track(source="test_vid/dji_export_1655129117122.mp4", show=True)
#results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")