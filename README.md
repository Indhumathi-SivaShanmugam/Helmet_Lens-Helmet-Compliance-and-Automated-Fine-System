## Helmet Lens- Helmet Compliance and Automated Fine System

## **Problem Statement**  
Many two-wheeler riders violate safety rules by not wearing helmets, leading to an increased risk of accidents and fatalities. Manual enforcement of traffic rules is challenging and resource-intensive. A smart, automated system is needed to detect helmetless riders, identify their vehicle's number plate, and issue fines efficiently to encourage compliance with traffic safety laws.

---

## **Project Idea**  
**Helmet Detection and Automated Fine System**  
This project aims to develop an AI-powered system that:  
1. Detects two-wheeler riders without helmets.  
2. Identifies and recognizes their vehicle's license plate.  
3. Sends an automated fine notification via email for non-compliance.  

---

## **Approach**  

The project is implemented using a YOLO (You Only Look Once) object detection model to detect two-wheeler riders without helmets and their number plates in real-time video feeds. For violation enforcement, the system integrates OCR to extract number plate details and triggers an alert system to automate fine notifications.  

---

### **Key Steps**  

1. **YOLO Model for Object Detection**  
   - Train a custom **YOLOv8** model to detect two-wheeler riders and classify them as wearing a helmet or not.  
   - Train the same model to detect vehicle license plates in the video.  

2. **OCR for Number Plate Recognition**  
   - Use **PaddleOCR** to extract text from the detected license plates.  
   - Preprocess detected license plate regions for better OCR accuracy.  

3. **Violation Detection**  
   - Analyze the output of the YOLO model to identify riders without helmets.  
   - Crop and process detected license plate regions for text recognition via OCR.  

4. **Automated Fine System**  
   - If a helmet violation is detected, store the violator's license plate number along with timestamp and location.  
   - Use a notification system (e.g., **Python SMTP library**) to send an email to the violator with the fine details and violation proof (e.g., annotated image or video).  

5. **Alert and Annotation System**  
   - Annotate video frames in real time with labels like "No Helmet Detected" and the extracted license plate number.  
   - Generate logs or visual evidence for further actions.  

6. **Visualization and Reporting**  
   - Use libraries like **Matplotlib** to visualize violation trends.  
   - Generate periodic reports for traffic authorities

---

## **Tech Stack**  
- **YOLOv8**: Helmet and license plate detection.  
- **PaddleOCR**: License plate recognition.  
- **OpenCV**: Image processing and video analysis.  
- **Matplotlib**: Visualization for reporting.  
- **Python**: Backend implementation for model inference and email automation.  

---

## **Progress/Status**  

### **Completed**  
- YOLOv8 model trained and functioning for helmet detection and license plate identification.  
- Initial integration of PaddleOCR.
![image](https://github.com/user-attachments/assets/36745c11-c70d-4bc5-9cad-e790a81f2a64) ![image](https://github.com/user-attachments/assets/c5cd1b58-c378-4d5d-9feb-01de12129530)




### **To Do**  
- Implement and refine the automated fine system (email alerts).  
- Optimize OCR and integrate it with the detection pipeline.  
- Test the system with real-world data for robustness.

---

## **Challenges Faced**  
1. **Integration of OCR with Detection Model**  
   - Ensuring seamless data flow between helmet detection, license plate detection, and PaddleOCR.  
   - Handling low-resolution or blurred license plates effectively.  

2. **Fine System Implementation**  
   - Automating the generation of fine notifications.  
   - Building a reliable database for storing violator records.  

3. **Real-world Testing**  
   - Adapting the system to varying lighting and environmental conditions for robust performance.  

---


