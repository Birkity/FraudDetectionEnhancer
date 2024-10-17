import matplotlib.pyplot as plt
import seaborn as sns

def analyze_categorical_features(data, cols):
    for col in cols:
        print(f"\nAnalyzing {col}:")
        freq = data[col].value_counts(normalize=True)
        print("Frequency Counts:", freq)

        perc = freq * 100
        print("Percentage Counts:", perc)

        unique_values = len(data[col].unique())
        print(f"Number of unique values: {unique_values}")

        plt.figure(figsize=(12, 6))
        sns.barplot(x=freq.index, y=freq.values)
        plt.title(f'Distribution of {col}')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

        if col == 'FraudResult':
            sns.heatmap(pd.crosstab(data['FraudResult'], data['ProductCategory']), annot=True, cmap='Blues')
            plt.title('Fraud vs Product Category')
            plt.tight_layout()
            plt.show()
