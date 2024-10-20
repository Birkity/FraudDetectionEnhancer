import pandas as pd

def create_transaction_frequency(df, group_col):
    df['transaction_frequency'] = df.groupby(group_col)[group_col].transform('count')
    return df


def extract_time_features(df, time_col):
    # Ensure the column is of datetime type
    if pd.api.types.is_datetime64_any_dtype(df[time_col]):
        df['hour_of_day'] = df[time_col].dt.hour
        df['day_of_week'] = df[time_col].dt.dayofweek
    else:
        # Try to parse the string values as datetime
        df[time_col] = pd.to_datetime(df[time_col], errors='coerce')
        
        # Handle any remaining non-parsable values
        df[time_col] = pd.to_datetime(df[time_col], errors='coerce')
        
        # Now extract hour and day of week
        df['hour_of_day'] = df[time_col].dt.hour
        df['day_of_week'] = df[time_col].dt.dayofweek
    
    return df
