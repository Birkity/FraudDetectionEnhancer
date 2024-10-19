from sklearn.preprocessing import StandardScaler, LabelEncoder

def scale_column(df, column):
    scaler = StandardScaler()
    df[f'scaled_{column}'] = scaler.fit_transform(df[[column]])
    return df

def encode_labels(df, columns):
    le = LabelEncoder()
    for col in columns:
        df[f'{col}_encoded'] = le.fit_transform(df[col])
    return df
