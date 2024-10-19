import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(data, column, title, xlabel, ylabel):
    sns.histplot(data[column], bins=50, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_count(data, column, title):
    sns.countplot(x=column, data=data)
    plt.title(title)
    plt.show()

def plot_boxplot(data, x_col, y_col, title, xlabel, ylabel):
    sns.boxplot(x=x_col, y=y_col, data=data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

