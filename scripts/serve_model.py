from flask import Flask, request, jsonify
import joblib
import logging

app = Flask(__name__)
credit_model = r'C:\Users\USER\Documents\OPLearning\10_Academy\Week_8_&_9\notebooks\mlruns\0\602c4dc095f64d92a816586eebc9593b\artifacts\Gradient Boosting - Credit\model.pkl'
fraud_model = r'C:\Users\USER\Documents\OPLearning\10_Academy\Week_8_&_9\notebooks\mlruns\0\db04e10872bc4082b67fed4588e00d45\artifacts\Random Forest - Fraud\model.pkl'

logging.basicConfig(filename='flask_logs.log', level=logging.INFO)

@app.route('/predict_fraud', methods=['POST'])
def predict_fraud():
    data = request.json
    prediction = fraud_model.predict(data)
    logging.info(f"Fraud Prediction: {prediction} for data: {data}")
    return jsonify({'prediction': prediction.tolist()})

@app.route('/predict_credit', methods=['POST'])
def predict_credit():
    data = request.json
    prediction = credit_model.predict(data)
    logging.info(f"Credit Prediction: {prediction} for data: {data}")
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
