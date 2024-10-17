def customer_aggregation(df):
    customer_aggregates = df.groupby('CustomerId').agg(
        TotalTransactionAmount=('Amount', 'sum'),
        AvgTransactionAmount=('Amount', 'mean'),
        TransactionCount=('TransactionId', 'count'),
        StdDevTransactionAmount=('Amount', 'std')
    ).reset_index()

    customer_aggregates['StdDevTransactionAmount'].fillna(0, inplace=True)
    return customer_aggregates

def transaction_aggregation(df):
    aggregated_df = df.groupby('CustomerId').agg({
        'Amount': ['sum', 'mean', 'std'],
        'Value': ['sum', 'mean', 'std'],
        'FraudResult': 'sum',  
        'TransactionId': 'count'
    }).reset_index()

    aggregated_df.columns = ['CustomerId', 'TotalAmount', 'AvgAmount', 'StdAmount', 'TotalValue', 'AvgValue', 'StdValue', 'FraudulentTransactionCount', 'TransactionCount']
    return aggregated_df
