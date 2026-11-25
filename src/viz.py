import pandas as pd
import matplotlib.pyplot as plt

## https://www.programiz.com/python-programming/pandas/methods/crosstab
## https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html

def smoker_age_percentage(df):
    """Calculating percentage of smoker by age group"""
    age_groups = pd.cut(
        df["age"],
        bins=[17, 29, 39, 49, 59, 69, 79, 90],
        labels=["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-90"]
    )

    percentage = pd.crosstab(
        age_groups,
        df["smoker"],
        normalize="index"
    ) * 100

    return percentage

def smoker_age_chart(df):
    """"Stacked bar chart of smoking percentage by age group"""

    percentage = smoker_age_percentage(df)

    ax = percentage[["Yes", "No"]].plot.bar(
        figsize=(10, 6),
        rot=0,
    )

    ax.set(
        title="Smoking status by age group",
        xlabel="Age group",
        ylabel="Percentage (%)",
        ylim=(0, 100),
        yticks=range(0, 101, 10)
    )

    ax.grid(axis="y", alpha=0.5)

    plt.show()