# 🌐 Fraud Detection Enhancer Project 🚀  
**Empowering E-commerce and Banking Transactions with Cutting-Edge Fraud Detection**  

---

## 📋 **Project Overview**  
This project, **Fraud Detection Enhancer**, aims to develop a robust fraud detection system for **Adey Innovations Inc.**, a leader in financial technology. The solution leverages **machine learning models**, **real-time monitoring**, and **interpretability techniques** to enhance fraud detection, balancing both **accuracy** and **transparency**.

---

## 🗂️ **Repository Structure**  
```bash
.
├── README.md              # 📄 Project overview and setup
├── notebooks/             # 📊 Jupyter notebooks for data analysis and preprocessing
├── data/                  # 📂 Datasets for fraud and IP address geolocation
├── Mlflow/                # 🏋️ Trained machine learning model files
├── scripts/                   # 🧑‍💻 Source code for feature engineering, model training, and API creation
└── dashboard.py             # 📈 Dash app for visualizations and real-time monitoring
```

---

## 🛠️ **Installation**  
Follow these steps to install and run the project.

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/Birkity/FraudDetectionEnhancer.git
cd fraud_detection_enhancer
```

### 2️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Dashboard**  
```bash
python dashboard/app.py
```

---

## ✅ **Tasks**  
### **Task 3: Feature Engineering**  
- Aggregated customer transactions and derived **temporal** and **geolocation features**.  
- Encapsulated transformations in `scripts/feature_engineering.py` for reusability.  

### **Task 4: Model Building and Evaluation**  
- Implemented models: **Logistic Regression, Random Forest, GBM, and MLP**.  
- Evaluated models with metrics like **accuracy, precision, recall, F1 score, and ROC-AUC**.  
- Code located in `scripts/model_training.py`.  

### **Task 5: Explainability and Dashboard**  
- Applied **SHAP** and **LIME** for model interpretability, ensuring transparency.  
- Developed a **real-time fraud monitoring dashboard** using Dash in `dashboard/app.py`.  
  Key dashboard features:  
  - **Fraud trends over time**  
  - **Geolocation-based fraud analysis**  
  - **Device and browser-based fraud cases**  

---

## 🔄 **General Project Flow**  
1. **Data Analysis**: Conducted EDA to identify patterns and key features for fraud detection.  
2. **Feature Engineering**: Created meaningful features to boost model performance.  
3. **Model Building**: Trained and evaluated multiple models across various metrics.  
4. **Explainability**: Used **SHAP** and **LIME** to interpret model decisions.  
5. **API & Dashboard**: Deployed APIs and dashboards for real-time fraud detection and insights.

---

## 🔮 **Future Work**  
- **Add Docker support** for seamless deployment.  
- **Enhance the dashboard** with additional user metrics and insights.  

---

## 📌 **Conclusion**  
This README provides a structured guide for **project installation**, **code flow**, and **key tasks**, helping users quickly understand and interact with the **Fraud Detection Enhancer** project.

---

✨ **Built with Passion by Birkity Yishak.** ✨  
