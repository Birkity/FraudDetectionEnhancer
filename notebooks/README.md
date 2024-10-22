# Task 1 - Data Analysis and Preprocessing

## Overview

This notebook, `task_1.ipynb`, contains the initial phase of the project, focused on data analysis and preprocessing. The objective of Task 1 is to gain a thorough understanding of the data and prepare it for subsequent stages of the fraud detection project, which involves building predictive models for identifying fraudulent transactions in e-commerce and bank credit data.

## Contents

The notebook is divided into the following sections:

### 1. Data Analysis

- **Data Understanding**: Describes the structure of the datasets used, including the number of rows, columns, data types, and initial observations.
- **Dataset Details**: Includes detailed information about the three datasets used in the project:
  - `creditcard.csv`: Contains transaction details for credit card transactions.
  - `Fraud_Data.csv`: Contains features related to online transactions.
  - `IpAddress_to_Country.csv`: Maps IP addresses to country codes, providing geolocation data.

### 2. Data Preprocessing

- **Handling Missing Values**: Identifies and addresses missing data in the datasets to ensure completeness.
- **Data Cleaning**: Processes and standardizes data for consistency, including format corrections and dealing with outliers.
- **Merging Datasets**: Combines `Fraud_Data` with `IpAddress_to_Country` to enrich transaction data with geolocation information, ensuring an accurate and comprehensive merge process.

### 3. Exploratory Data Analysis (EDA)

- **Univariate Analysis**: Examines the distribution of individual variables to identify patterns and outliers.
- **Bivariate Analysis**: Explores relationships between pairs of features, focusing on identifying key factors influencing fraud.
- **Correlation Analysis**: Analyzes the correlation between numerical features to highlight significant relationships and potential predictors of fraud.

### 4. Key Insights

- **Data Insights**: Discusses important patterns observed in the data, including trends in transaction amounts and the frequency of fraudulent transactions.
- **Correlation Findings**: Highlights key correlations between transaction features and fraud, particularly the strong correlation between 'Amount', 'Value', and 'FraudResult'.
- **Challenges and Next Steps**: Summarizes challenges faced during data preprocessing and outlines the next steps for feature engineering and model building.

## How to Use

1. Clone the repository and navigate to the `notebooks` directory.
2. Open the `task_1.ipynb` file in Jupyter Notebook or Jupyter Lab.
3. Ensure that the required datasets (`creditcard.csv`, `Fraud_Data.csv`, `IpAddress_to_Country.csv`) are available in the `data` folder.
4. Run each cell sequentially to reproduce the analysis and preprocessing steps.

## Prerequisites

- **Python Version**: 3.8+
- **Libraries Used**: `pandas`, `numpy`, `matplotlib`, `seaborn`
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```
- Make sure Jupyter Notebook is installed and set up in your environment.

## Results & Next Steps

The completion of Task 1 sets the foundation for further feature engineering and model training. The detailed analysis and cleaned datasets will be used in subsequent tasks to create predictive models, ensuring that the project progresses smoothly toward effective fraud detection.

---

## 🔍 Overview of Task 2

### 🎯 Objective:

- The main goal is to build, train, and evaluate models to accurately classify fraudulent transactions using cleaned and preprocessed datasets.

### 💡 Key Steps:

1. **Data Preparation**:

   - Data cleaning and preprocessing: handled missing values, normalized numerical features, and encoded categorical variables.
   - Train-test split: 80% for training and 20% for testing.

2. **Model Selection**:

   - **Logistic Regression**
   - **Random Forest**
   - **Gradient Boosting Machines (GBM)**
   - **Deep Learning models**: Convolutional Neural Network (CNN), Recurrent Neural Network (RNN), Long Short-Term Memory (LSTM)

3. **Model Training and Evaluation**:

   - Trained each model using `model_training.py` or through the `task_2.ipynb`.
   - Evaluated models using metrics like **Accuracy**, **Precision**, **Recall**, **F1 Score**, and **ROC-AUC**.
   - Used **EarlyStopping** to prevent overfitting in deep learning models.

4. **Logging with MLflow**:
   - Tracked model training experiments, performance metrics, and saved models using **MLflow**.

---

## 🧠 Model Performance Summary

| **Model**           | **Accuracy** | **Precision** | **Recall** | **F1 Score** | **ROC-AUC** |
| ------------------- | ------------ | ------------- | ---------- | ------------ | ----------- |
| Logistic Regression | 0.947        | 0.92          | 0.75       | 0.83         | 0.95        |
| Random Forest       | 0.964        | 0.93          | 0.82       | 0.87         | 0.97        |
| GBM                 | 0.969        | 0.94          | 0.85       | 0.89         | 0.98        |
| CNN                 | 0.924        | 0.95          | 0.21       | 0.35         | 0.76        |
| LSTM                | 0.956        | 0.99          | 0.54       | 0.70         | 0.76        |

---

## 📝 Detailed Model Training

### 1. **Logistic Regression**:

- Used as a baseline model for comparison.
- Achieved **94.7% accuracy** on the test set with a balanced trade-off between **precision** and **recall**.

### 2. **Random Forest**:

- Outperformed the baseline model with an accuracy of **96.4%**.
- Good at capturing complex patterns but takes more time to train.

### 3. **Gradient Boosting Machines (GBM)**:

- Achieved the best performance among tree-based models.
- Suitable for handling class imbalances and providing robust predictions.

### 4. **Convolutional Neural Network (CNN)**:

- Captured temporal relationships in transaction sequences.
- Higher precision but low recall, indicating a need for further tuning.

### 5. **LSTM (Long Short-Term Memory)**:

- Designed for capturing long-term dependencies in transaction data.
- Balanced performance with **95.6% accuracy** and an **F1 score** of **0.70**.

---

## 🚀 How to Use the Models

1. **Training Models**:

   - Run the Jupyter notebook `task_2.ipynb` or the Python script:
     ```bash
     python src/model_training.py
     ```

2. **Evaluate on Custom Data**:
   - Load your data into the same format as the `creditcard_cleaned.csv` or `fraud_data_cleaned.csv`.
   - Preprocess the data using `src/preprocessing.py` and use the saved models from the `models/saved_models/` directory for prediction.

---

---

## 📬 Contact

For any queries or suggestions, please reach out to:

- **Name:** Birkity Yishak
- **Email:** lily.yishak2@gmail.com

---

Feel free to adjust the content to better match the specifics of my project!
