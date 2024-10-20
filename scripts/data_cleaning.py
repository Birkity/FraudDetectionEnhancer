import pandas as pd

def handle_missing_values(df):
    return df.isnull().sum()

def drop_duplicates(df):
    if isinstance(df, pd.DataFrame):
        df.drop_duplicates(inplace=True)
    else:
        print("The input is not a DataFrame.")
    return df

def convert_to_datetime(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col])
    return df

