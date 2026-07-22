# 📦 Supply Chain Delivery Delay Prediction using Machine Learning

## 📖 Project Overview

Supply Chain Delivery Delay Prediction is a Machine Learning project that predicts whether an e-commerce shipment is likely to be **Delayed** or **Delivered On Time** based on shipment details such as delivery partner, vehicle type, delivery mode, weather conditions, distance, and package weight.

The project uses a Random Forest Classifier and is deployed as an interactive web application using Streamlit.

---

## 🎯 Problem Statement

Delivery delays negatively impact customer satisfaction, increase operational costs, and affect supply chain efficiency. Businesses need an intelligent system that can identify shipments at risk of delay before delivery.

---

## 🎯 Objectives

- Predict delivery delays using Machine Learning.
- Analyze shipment data to identify important factors affecting delivery.
- Build an accurate classification model.
- Deploy the trained model using Streamlit.
- Provide real-time delivery status prediction.

---

## 📊 Dataset

- Dataset Format: CSV
- Total Records: 25,000
- Records Used for Training: 10,000
- Number of Columns: 15

### Features Used

- Delivery Partner
- Vehicle Type
- Delivery Mode
- Weather Condition
- Distance (km)
- Package Weight (kg)

### Target Variable

- Delayed (Yes/No)

---

## ⚙️ Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Feature Encoding
4. Feature Scaling
5. Model Training
6. Model Evaluation
7. Save Model
8. Streamlit Deployment

---

## 🧠 Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

**Model Parameters**

- n_estimators = 100
- max_depth = 8
- random_state = 1

---

## 📈 Model Performance

- Accuracy: **88.15%**
- Train-Test Split: **80 : 20**

---

## 💻 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## 📁 Project Structure

```
ML_Project/
│
├── delivery_model.pkl
├── stream.py
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Shrutika12345/ML_Project.git
```

Move into the project folder

```bash
cd ML_Project
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run stream.py
```

---

## 🚀 Live Demo

Streamlit App

https://shrutika-ml.streamlit.app/

---

## 📷 Application Features

- User-friendly interface
- Shipment detail input form
- Real-time prediction
- Instant delivery status
- Machine Learning powered prediction

---

## 🔮 Future Enhancements

- Train using larger datasets.
- Compare multiple Machine Learning algorithms.
- Improve prediction accuracy.
- Add additional evaluation metrics such as Precision, Recall, F1-Score, and Confusion Matrix.
- Integrate live logistics data.

---

## 👩‍💻 Author

**Shrutika Gaikwad**

GitHub: https://github.com/Shrutika12345

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.
