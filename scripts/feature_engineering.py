import pandas as pd

def create_transaction_frequency(df, group_col):
    df['transaction_frequency'] = df.groupby(group_col)[group_col].transform('count')
    return df

def extract_time_features(df, time_col):
    df['hour_of_day'] = df[time_col].dt.hour
    df['day_of_week'] = df[time_col].dt.dayofweek
    return df
