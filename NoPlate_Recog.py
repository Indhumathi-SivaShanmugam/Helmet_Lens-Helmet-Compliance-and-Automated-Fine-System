from paddleocr import PaddleOCR
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Load the trained YOLO model
model_path = '/content/drive/MyDrive/Bike_extract/Bike/runs/train/yolov8_helmet_detection/weights/best.pt'
model = YOLO(model_path)

# Path to the test image
test_image_path = '/content/drive/MyDrive/Bike_extract/Bike/val/images/new80.jpg'

# Run inference using YOLO
results = model.predict(source=test_image_path, show=True, save=False)
image = cv2.imread(test_image_path)

# Iterate through YOLO results
for result in results[0].boxes:
    # Get bounding box coordinates
    x1, y1, x2, y2 = map(int, result.xyxy[0])

    # Ensure bounding box is within image dimensions
    height, width, _ = image.shape
    x1, y1, x2, y2 = max(0, x1), max(0, y1), min(width, x2), min(height, y2)

    # Crop detected region
    cropped_plate = image[y1:y2, x1:x2]

    # Convert BGR to RGB for PaddleOCR
    cropped_plate_rgb = cv2.cvtColor(cropped_plate, cv2.COLOR_BGR2RGB)

    # Perform OCR
    ocr_results = ocr.ocr(cropped_plate_rgb, cls=True)

    # Initialize detected_text to indicate no text by default
    detected_text = "No text detected"

    # Check if OCR returned results
    if ocr_results and isinstance(ocr_results, list) and len(ocr_results) > 0:
        # Check if any text was detected
        if len(ocr_results[0]) > 0:
            # Extract detected text
            detected_text = ''.join([line[1][0] for line in ocr_results[0]])
            print("Detected Text:", detected_text)
        else:
            print("No text detected in the cropped image.")
    else:
        print("OCR returned no valid results.")

    # Display the cropped image and detected text
    plt.figure()
    plt.imshow(cv2.cvtColor(cropped_plate, cv2.COLOR_BGR2RGB))
    plt.title(f"Detected Text: {detected_text}")
    plt.axis('off')
    plt.show()
