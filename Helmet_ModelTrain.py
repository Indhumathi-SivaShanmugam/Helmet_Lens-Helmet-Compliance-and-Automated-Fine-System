from ultralytics import YOLO

# Load a YOLOv8 model
model = YOLO('yolov8n.pt')  # Replace with 'yolov8s.pt' or larger models if needed

# Train the model
model.train(
    data='/content/drive/MyDrive/Bike_extract/Bike/data.yaml',  # Path to YAML file
    epochs=50,  # Number of epochs
    imgsz=640,  # Image size
    batch=16,  # Batch size
    project='/content/drive/MyDrive/Bike_extract/Bike/runs/train',  # Directory to save training results
    name='yolov8_helmet_detection',  # Name of the training session
    exist_ok=True  # Allow overwriting if there's a previous training run
)
