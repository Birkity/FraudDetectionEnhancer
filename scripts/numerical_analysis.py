import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_numerical_features(data, cols):
    results = {}
    
    for col in cols:
        print(f"\nAnalyzing {col}:")
        stats = data[col].describe()
        print("Descriptive Statistics:", stats)

        percentiles = data[col].quantile([0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
        print("Percentiles:", percentiles)

        skew = data[col].skew()
        kurt = data[col].kurtosis()
        print(f"Skewness: {skew:.2f}, Kurtosis: {kurt:.2f}")

        q75, q25 = np.percentile(data[col], [75, 25])
        iqr = q75 - q25
        print(f"IQR: {iqr:.2f}")

        mode = data[col].mode()
        print(f"Mode: {mode.tolist()}")

        std_dev = data[col].std()
        print(f"Standard Deviation: {std_dev:.2f}")

        mad = np.median(np.abs(data[col] - data[col].median()))
        print(f"MAD: {mad:.2f}")

        cv = std_dev / data[col].mean()
        print(f"CV: {cv:.2f}")

        plt.figure(figsize=(12, 6))
        sns.histplot(data[col], kde=True, bins=30)
        plt.title(f'Distribution of {col}')
        plt.show()

    return results
