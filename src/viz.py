import pandas as pd
import matplotlib.pyplot as plt

## https://www.programiz.com/python-programming/pandas/methods/crosstab

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
