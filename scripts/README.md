# Data Analysis and Preprocessing Scripts

Welcome to the **Data Analysis and Preprocessing** scripts for the `Fraud Detection Enhancer` project! These Python scripts help streamline the data processing pipeline, making it easier to analyze, clean, and prepare datasets for the next phases of fraud detection, including feature engineering, model training, and evaluation.

## Overview

This repository includes a collection of modular scripts designed for various data processing tasks. Each script serves a specific function in the data analysis and preprocessing pipeline, ensuring a clean, efficient, and reusable workflow. Below is a breakdown of each script, its purpose, and how to use it.

## Folder Structure

```
scripts/
├── data_loading.py
├── data_cleaning.py
├── eda.py
├── feature_engineering.py
├── scaling_encoding.py
├── geolocation.py
├── utils.py
```

## Script Descriptions

### 1. `data_loading.py`

**Purpose**: This script handles the loading of datasets from CSV files into pandas DataFrames. It simplifies the data import process, making it easy to load different datasets required for analysis.

**Functions**:

- `load_data(file_path)`: Loads a CSV file into a DataFrame.

**Example Usage**:

```python
from scripts.data_loading import load_data

df_creditcard = load_data('../data/creditcard.csv')
df_fraud_data = load_data('../data/Fraud_Data.csv')
```

---

### 2. `data_cleaning.py`

**Purpose**: This script focuses on handling missing values, dropping duplicates, and converting columns to appropriate data types. It ensures the data is clean and ready for analysis.

**Functions**:

- `handle_missing_values(df)`: Returns the count of missing values in each column.
- `drop_duplicates(df)`: Removes duplicate rows from a DataFrame.
- `convert_to_datetime(df, columns)`: Converts specified columns to datetime format.

**Example Usage**:

```python
from scripts.data_cleaning import handle_missing_values, drop_duplicates, convert_to_datetime

df_creditcard = drop_duplicates(df_creditcard)
missing_values = handle_missing_values(df_creditcard)
df_fraud_data = convert_to_datetime(df_fraud_data, ['signup_time', 'purchase_time'])
```

---

### 3. `eda.py`

**Purpose**: This script contains functions for conducting Exploratory Data Analysis (EDA), including visualizations of distributions and relationships between variables. It helps identify patterns, outliers, and trends in the data.

**Functions**:

- `plot_histogram(data, column, title, xlabel, ylabel)`: Plots a histogram of the specified column.
- `plot_count(data, column, title)`: Creates a count plot for a categorical variable.
- `plot_boxplot(data, x_col, y_col, title, xlabel, ylabel)`: Generates a boxplot for analyzing distributions.

**Example Usage**:

```python
from scripts.eda import plot_histogram, plot_count

plot_histogram(df_creditcard, 'Amount', 'Distribution of Transaction Amounts', 'Amount', 'Frequency')
plot_count(df_fraud_data, 'class', 'Distribution of Fraud Classes')
```

---

### 4. `feature_engineering.py`

**Purpose**: This script includes functions for creating new features and transforming existing ones. It enables the generation of additional information that can enhance model performance during training.

**Functions**:

- `create_transaction_frequency(df, group_col)`: Creates a feature representing the transaction frequency per user.
- `extract_time_features(df, time_col)`: Extracts hour of the day and day of the week from a timestamp column.

**Example Usage**:

```python
from scripts.feature_engineering import create_transaction_frequency, extract_time_features

df_fraud_data = create_transaction_frequency(df_fraud_data, 'user_id')
df_fraud_data = extract_time_features(df_fraud_data, 'purchase_time')
```

---

### 5. `scaling_encoding.py`

**Purpose**: This script standardizes numerical features and encodes categorical features. It is crucial for preparing data before feeding it into machine learning models.

**Functions**:

- `scale_column(df, column)`: Scales a numerical column using `StandardScaler`.
- `encode_labels(df, columns)`: Encodes categorical features using `LabelEncoder`.

**Example Usage**:

```python
from scripts.scaling_encoding import scale_column, encode_labels

df_creditcard = scale_column(df_creditcard, 'Amount')
df_fraud_data = encode_labels(df_fraud_data, ['source', 'browser', 'sex'])
```

---

### 6. `geolocation.py`

**Purpose**: This script merges datasets to perform geolocation analysis, linking IP addresses with country information for a deeper understanding of transaction data.

**Functions**:

- `merge_ip_country(fraud_data, ip_country_data)`: Merges IP address information with country data using a range-based join.

**Example Usage**:

```python
from scripts.geolocation import merge_ip_country

merged_data = merge_ip_country(df_fraud_data, df_IpAddress)
```

---

### 7. `utils.py`

**Purpose**: This utility script contains helper functions for saving processed DataFrames and other reusable functionalities.

**Functions**:

- `save_data(df, file_path)`: Saves a DataFrame to a CSV file.

**Example Usage**:

```python
from scripts.utils import save_data

save_data(merged_data, '../data/merged_result.csv')
```

---

## How to Use

1. Clone the repository and navigate to the project directory.
2. Ensure the data files (`creditcard.csv`, `Fraud_Data.csv`, `IpAddress_to_Country.csv`) are available in the `data` folder.
3. Use the functions from each script as needed in your analysis notebooks or other parts of the project.

## Benefits of Using Modular Scripts

- **Reusability**: Each function can be used across different parts of the project, reducing code duplication.
- **Maintainability**: It's easier to update or debug specific functionalities.
- **Readability**: Breaks down complex processes into smaller, understandable chunks.

## Next Steps

With the data prepared using these scripts, you can proceed to the next phases of the project, such as model training, evaluation, and deployment. The cleaned and processed data is ready for analysis and feature extraction, making the transition to machine learning models seamless.

## Contributing

Feel free to contribute to this project by adding new functionalities or improving existing ones. Please ensure that your contributions align with the existing coding style and structure.

---

This `README.md` should provide a comprehensive guide to using your scripts effectively, making it easy for collaborators or future users to understand the structure and purpose of each component.
