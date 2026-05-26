import matplotlib.pyplot as plt
import seaborn as sns



def check_missing_values(df):
    missing = df.isnull().sum()

    return missing[missing > 0]



def calculate_loss_ratio(df):
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"]

    return df

def calculate_margin(df):
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]

    return df



def plot_histogram(df, column):
    plt.figure(figsize=(8, 5))

    sns.histplot(df[column], kde=True)

    plt.title(f"Distribution of {column}")

    plt.show()



def plot_boxplot(df, column):   
    plt.figure(figsize=(8, 5))

    sns.boxplot(x=df[column])

    plt.title(f"Boxplot of {column}")

    plt.show()



def plot_correlation(df):
    numerical = df.select_dtypes(include="number")

    plt.figure(figsize=(12, 8))

    sns.heatmap(numerical.corr(), annot=True, cmap="coolwarm")

    plt.title("Correlation Heatmap")

    plt.show()