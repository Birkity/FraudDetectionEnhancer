from flask import Flask, request, jsonify
import joblib
import logging
import pickle
import pandas as pd

app = Flask(__name__)
credit_model_path = r'C:\Users\USER\Documents\OPLearning\10_Academy\Week_8_&_9\notebooks\mlruns\0\602c4dc095f64d92a816586eebc9593b\artifacts\Gradient Boosting - Credit\model.pkl'
fraud_model_path = r'C:\Users\USER\Documents\OPLearning\10_Academy\Week_8_&_9\notebooks\mlruns\0\db04e10872bc4082b67fed4588e00d45\artifacts\Random Forest - Fraud\model.pkl'

logging.basicConfig(filename='flask_logs.log', level=logging.INFO)

@app.route('/predict_fraud', methods=['POST'])
def predict_fraud():
    try:
        data = request.get_json()
        
        expected_columns = [
            "user_id", "purchase_value", "source", "browser", "sex", "age",
            "ip_address", "signup_month", "signup_day", "purchase_month", 
            "purchase_day", "purchase_hour", "time_diff", "device_id_encoded"
        ]
        
        if not all(col in data for col in expected_columns):
            raise ValueError("Missing required columns")
        
        data_df = pd.DataFrame([data])  
        data_df = data_df[expected_columns]

        prediction = fraud_model.predict(data_df)
        
        return jsonify({'fraud_prediction': int(prediction[0])})
    
    except ValueError as ve:
        app.logger.error(f"Invalid input: {ve}")
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        app.logger.error(f"Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/predict_credit', methods=['POST'])
def predict_credit():
    try:
        data = request.get_json()

        expected_columns = [
            "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9",
            "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17",
            "V18", "V19", "V20", "V21", "V22", "V23", "V24", "V25",
            "V26", "V27", "V28", "Amount", "transaction_hour", 
            "transaction_day", "transaction_month"
        ]
        
        if not all(col in data for col in expected_columns):
            raise ValueError("Missing required columns")
        
        data_df = pd.DataFrame([data])
        data_df = data_df[expected_columns]

        prediction = credit_model.predict(data_df)

        return jsonify({"fraud_prediction": int(prediction[0])})

    except ValueError as ve:
        app.logger.error(f"Invalid input: {ve}")
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        app.logger.error(f"Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with open(fraud_model_path, 'rb') as f:
        fraud_model = pickle.load(f)

    with open(credit_model_path, 'rb') as f:
        credit_model = pickle.load(f)

    app.run(debug=True)  
