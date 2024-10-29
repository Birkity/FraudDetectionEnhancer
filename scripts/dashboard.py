import dash
from dash import dcc, html, Input, Output
import requests
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Fraud Detection Dashboard"),
    dcc.Graph(id='fraud-trend-chart'),
    dcc.Graph(id='geographical-fraud-chart'),
    dcc.Graph(id='device-browser-fraud-chart')
])

@app.callback(Output('fraud-trend-chart', 'figure'), Input('fraud-trend-chart', 'id'))
def update_fraud_trend_chart(_):
    try:
        response = requests.get("http://127.0.0.1:5000/api/fraud_trends")
        response.raise_for_status()
        trend_data = response.json()
        df = pd.DataFrame(trend_data)
        fig = px.line(df, x='purchase_date', y='fraud_cases', title="Fraud Trends Over Time")
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching fraud trend data: {e}")
        fig = px.line(title="Fraud Trends Over Time - No Data Available")
    return fig


@app.callback(Output('geographical-fraud-chart', 'figure'), Input('geographical-fraud-chart', 'id'))
def update_geographical_fraud_chart(_):
    try:
        response = requests.get("http://127.0.0.1:5000/api/geographic_fraud")
        response.raise_for_status()
        geo_data = response.json()
        df = pd.DataFrame(geo_data)
        fig = px.bar(df, x='ip_address', y='fraud_cases', title="Geographical Fraud Cases")
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching geographical fraud data: {e}")
        fig = px.bar(title="Geographical Fraud Cases - No Data Available")
    return fig


@app.callback(Output('device-browser-fraud-chart', 'figure'), Input('device-browser-fraud-chart', 'id'))
def update_device_fraud_chart(_):
    try:
        response = requests.get("http://127.0.0.1:5000/api/device_browser_fraud")
        response.raise_for_status()
        data = response.json()
        
        # Create two DataFrames for device and browser data
        device_df = pd.DataFrame(list(data['device_fraud'].items()), columns=['device', 'fraud_cases'])
        browser_df = pd.DataFrame(list(data['browser_fraud'].items()), columns=['browser', 'fraud_cases'])
        
        fig = px.pie(device_df, names='device', values='fraud_cases', title="Fraud Cases by Device")
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching device fraud data: {e}")
        fig = px.pie(title="Fraud Cases by Device - No Data Available")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
