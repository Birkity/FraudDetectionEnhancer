from sklearn.preprocessing import StandardScaler, LabelEncoder

def scale_column(df, column):
    scaler = StandardScaler()
    df[f'scaled_{column}'] = scaler.fit_transform(df[[column]])
    return df

def encode_labels(df, columns):
    le = LabelEncoder()
    
    encoded_data = []
    for col in columns:
        encoded_col = f'{col}_encoded'
        encoded_series = le.fit_transform(df[col])
        encoded_data.append(encoded_series)
    
    encoded_df = pd.DataFrame(encoded_data).T
    
    encoded_df.index = columns
    
    return encoded_df
