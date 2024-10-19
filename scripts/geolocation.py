import pandas as pd

def merge_ip_country(fraud_data, ip_country_data):
    fraud_data['ip_address'] = fraud_data['ip_address'].astype(int)
    ip_country_data['lower_bound_ip_address'] = ip_country_data['lower_bound_ip_address'].astype(int)
    ip_country_data['upper_bound_ip_address'] = ip_country_data['upper_bound_ip_address'].astype(float).astype(int)
    ip_country_data = ip_country_data.sort_values(by='lower_bound_ip_address')

    merged_df = pd.merge_asof(
        fraud_data.sort_values('ip_address'), 
        ip_country_data[['country', 'lower_bound_ip_address', 'upper_bound_ip_address']], 
        left_on='ip_address', 
        right_on='lower_bound_ip_address',
        direction='backward'
    )
    merged_df.drop(['ip_address'], axis=1, inplace=True)
    return merged_df

