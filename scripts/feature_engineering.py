import pandas as pd

def add_time_features(df):
    df['TransactionHour'] = df['TransactionStartTime'].dt.hour
    df['TransactionDay'] = df['TransactionStartTime'].dt.day
    df['TransactionMonth'] = df['TransactionStartTime'].dt.month
    df['TransactionYear'] = df['TransactionStartTime'].dt.year
    return df

def add_risk_segment(df):
    df['RiskSegment'] = pd.cut(df['Amount'], bins=[0, 100, 1000, 10000, 100000], labels=['Low', 'Medium', 'High', 'Very High'])
    return df
