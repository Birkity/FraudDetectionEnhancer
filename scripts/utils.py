import pandas as pd

def save_data(df, file_path):
    df.to_csv(file_path, index=False)


