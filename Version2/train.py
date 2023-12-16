from ultralytics import YOLO


# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data='data/coco128.yaml', epochs=50)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model('datasets/coco128/images/test/dji_export_1655129128508.jpg')

# Export the model to ONNX format
success = model.export()