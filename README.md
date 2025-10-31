# 🖋️ Handwritten Digit Recognition App

This project is a **Streamlit web application** that recognizes handwritten digits drawn on an interactive canvas.  
It uses a **TensorFlow CNN model (`handwritten.h5`)** trained on the **MNIST dataset** to predict digits (0–9) and allows users to test multiple drawings while checking their overall prediction accuracy.

---

## 🚀 Features

✅ Draw any digit (0–9) on an interactive canvas  
✅ Predict the digit instantly using a trained deep learning model  
✅ Enter the correct digit to record prediction results  
✅ View the **accuracy of predictions** based on your drawings  
✅ Clear all results with one click  

---

## 🧠 Tech Stack

- **Python 3.8+**
- **TensorFlow / Keras** – Model for digit recognition  
- **Streamlit** – Web framework for the UI  
- **PIL (Pillow)** – Image preprocessing  
- **NumPy & Matplotlib** – Numerical operations & visualization  
- **streamlit-drawable-canvas** – Interactive drawing board  

---
## Model Information

The handwritten.h5 model is a CNN trained on the MNIST dataset consisting of 70,000 grayscale images of handwritten digits (28x28 pixels).
It classifies input images into one of 10 classes (0–9).
give this properly

---

## 📦 Installation Guide
```bash
### 1️. Clone this repository

git clone https://github.com/pruthvishetty1789/handwritten-digit-recognition.git
cd handwritten-digit-recognition


 2. Create and activate a virtual environment
On Windows
python -m venv env
env\Scripts\activate

On macOS / Linux
python3 -m venv env
source env/bin/activate

 3. Install dependencies
pip install tensorflow pillow numpy pandas matplotlib streamlit streamlit-drawable-canvas

 4.Run
streamlit run app.py


