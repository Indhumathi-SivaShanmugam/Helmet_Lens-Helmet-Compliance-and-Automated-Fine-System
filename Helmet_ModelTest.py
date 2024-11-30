from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load the trained model
model_path = '/content/drive/MyDrive/Bike_extract/Bike/runs/train/yolov8_helmet_detection/weights/best.pt'
model = YOLO(model_path)

# Path to the test image
test_image_path = '/content/drive/MyDrive/Bike_extract/Bike/val/images/new80.jpg'  # Replace with your test image path

# Run inference
results = model.predict(source=test_image_path, show=True)

# Display the results
plt.imshow(cv2.cvtColor(results[0].plot(), cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
