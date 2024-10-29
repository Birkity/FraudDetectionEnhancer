import pandas as pd
from flask import Flask, jsonify

#fraud_data = pd.read_csv(r'C:\Users\USER\Documents\OPLearning\10_Academy\Week_8_&_9\data\Fraud_Data.csv')
app = Flask(__name__)

fraud_data = pd.read_csv(r'C:\Users\USER\Documents\OPLearning\10_Academy\Week_8_&_9\data\Fraud_Data.csv', parse_dates=['signup_time', 'purchase_time'])

@app.route('/api/summary', methods=['GET'])
def get_summary():
    total_transactions = len(fraud_data)
    total_fraud_cases = fraud_data[fraud_data['class'] == 1].shape[0]
    fraud_percentage = (total_fraud_cases / total_transactions) * 100

    return jsonify({
        'total_transactions': total_transactions,
        'total_fraud_cases': total_fraud_cases,
        'fraud_percentage': fraud_percentage
    })

@app.route('/api/fraud_trends', methods=['GET'])
def fraud_trends():
    fraud_data['purchase_date'] = fraud_data['purchase_time'].dt.date
    trends = fraud_data[fraud_data['class'] == 1].groupby('purchase_date').size()

    trends_json = trends.reset_index().rename(columns={0: 'fraud_cases'}).to_dict(orient='records')
    return jsonify(trends_json)

@app.route('/api/device_browser_fraud', methods=['GET'])
def device_browser_fraud():
    device_fraud = fraud_data[fraud_data['class'] == 1].groupby('device_id').size()
    browser_fraud = fraud_data[fraud_data['class'] == 1].groupby('browser').size()

    return jsonify({
        'device_fraud': device_fraud.to_dict(),
        'browser_fraud': browser_fraud.to_dict()
    })

if __name__ == '__main__':
    app.run(debug=True)
