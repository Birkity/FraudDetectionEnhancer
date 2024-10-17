import seaborn as sns
import matplotlib.pyplot as plt

def analyze_correlations(df, numerical_cols):
    correlation_matrix = df[numerical_cols].corr(method='pearson')
    print("Correlation Matrix:\n", correlation_matrix)

    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)
    plt.title('Correlation Matrix Heatmap')
    plt.tight_layout()
    plt.show()
