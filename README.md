🧠 Brain Tumor Detection using YOLOv12

A deep-learning model trained to detect brain tumors using the latest YOLOv12 architecture.
This repository contains the trained model, inference notebook, and sample test images for quick evaluation.


Project Structure
<br><br/>
├── best.pt                 # Trained YOLOv12 model
<br><br/>
├── Brain_tumor.ipynb       # Training notebook
<br><br/>
├── Test.ipynb              # Inference notebook (runs predictions)
<br><br/>
├── test_images/            # Sample test images
<br><br/>
├── README.md               # Project documentation
<br><br/>



⚙️ Requirements

This project runs on Google Colab or locally with:

Python 3.10+

PyTorch (CUDA recommended)

Ultralytics YOLOv12

Install YOLOv12 using:

pip install ultralytics




🚀 Running Inference (Predict Tumor)

You can run predictions in Test.ipynb.

Example inference code:

from ultralytics import YOLO

# Load trained model
model = YOLO("Brain-Tumor-Detection/best.pt")

# Predict on an image
results = model("Brain-Tumor-Detection/test1.jpg")

# Display result
results[0].show()


<img width="753" height="755" alt="image" src="https://github.com/user-attachments/assets/f5b518c3-983d-4452-b2da-3a3e36463eaf" />





https://github.com/user-attachments/assets/35e2736a-0361-4c90-a5da-b2ec3f13ae20








📦 Running Locally

Clone the repo:

!git clone https://github.com/naksh2729-ai/Brain-Tumor-Detection
cd Brain-Tumor-Detection


Run inference:

python inference.py --image test_images/sample.jpg --model best.pt


🧩 What This Model Does

✔ Detects presence of a tumor
<br><br/>
✔ Localizes the tumor region with bounding boxes
<br><br/>
✔ Trained on MRI brain scans

🙌 Credits

YOLOv12 by Ultralytics

Dataset: Brain MRI Tumor Dataset 
