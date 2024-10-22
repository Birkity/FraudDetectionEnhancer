
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import mlflow
import mlflow.sklearn
import warnings


warnings.filterwarnings("ignore")


def load_data(file_path):
    """Load the dataset from a specified CSV file."""
    return pd.read_csv(file_path)


def preprocess_data(df):
    """Preprocess the dataset."""
    s
    categorical_features = ['source_encoded', 'browser_encoded', 'sex_encoded', 'country_encoded']
    numerical_features = ['scaled_purchase_value']

    X = df.drop(columns=['class'])  
    y = df['class']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(), categorical_features)
        ]
    )

    return X_train, X_test, y_train, y_test, preprocessor


def train_model(model, preprocessor, X_train, y_train):
    """Train the specified model using preprocessed training data."""
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                ('model', model)])

    
    pipeline.fit(X_train, y_train)
    return pipeline


def evaluate_model(model, X_test, y_test):
    """Evaluate the model's performance on the test set."""
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)

    return accuracy, precision, recall, f1, roc_auc


def log_model_with_mlflow(model, model_name, accuracy, precision, recall, f1, roc_auc):
    
    mlflow.start_run()
    mlflow.log_param("model", model_name)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)
    mlflow.log_metric("roc_auc", roc_auc)

    
    mlflow.sklearn.log_model(model, model_name)
    mlflow.end_run()


def main():
    
    df = load_data('data/fraud_data_cleaned.csv')  # Update the path as needed

    
    X_train, X_test, y_train, y_test, preprocessor = preprocess_data(df)

    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Random Forest': RandomForestClassifier(),
        'Gradient Boosting': GradientBoostingClassifier()
    }

  
    for model_name, model in models.items():
        print(f"Training {model_name}...")
        trained_model = train_model(model, preprocessor, X_train, y_train)

       
        accuracy, precision, recall, f1, roc_auc = evaluate_model(trained_model, X_test, y_test)
        
        
        log_model_with_mlflow(trained_model, model_name, accuracy, precision, recall, f1, roc_auc)

        
        print(f"{model_name} - Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, "
              f"F1 Score: {f1:.4f}, ROC-AUC: {roc_auc:.4f}\n")


if __name__ == "__main__":
    main()
