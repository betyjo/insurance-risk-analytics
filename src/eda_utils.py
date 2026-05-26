import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------
# BASIC DATA CHECKS
# ---------------------------

def data_summary(df: pd.DataFrame):
    """Print basic info and stats."""
    print(df.info())
    print(df.describe(include="all"))


def missing_values(df: pd.DataFrame):
    """Return missing value counts."""
    return df.isnull().sum().sort_values(ascending=False)


# ---------------------------
# FEATURE ENGINEERING
# ---------------------------

def add_risk_metrics(df: pd.DataFrame):
    """
    Adds:
    - LossRatio
    - Margin
    """

    df = df.copy()

    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"]
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]

    return df


# ---------------------------
# PLOTS
# ---------------------------

def hist_plot(df, col):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()


def box_plot(df, col):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()


def bar_plot(df, col):
    plt.figure(figsize=(10, 5))
    df[col].value_counts().plot(kind="bar")
    plt.title(col)
    plt.xticks(rotation=45)
    plt.show()


def correlation_plot(df):
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.select_dtypes(include="number").corr(),
                annot=True,
                cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()


# ---------------------------
# BUSINESS INSIGHTS HELPERS
# ---------------------------

def loss_ratio_by_group(df, group_col):
    return df.groupby(group_col)["LossRatio"].mean().sort_values(ascending=False)


def claims_by_group(df, group_col):
    return df.groupby(group_col)["TotalClaims"].mean().sort_values(ascending=False)


def trend_over_time(df, time_col="TransactionMonth"):
    return df.groupby(time_col)["TotalClaims"].sum()