import pandas as pd
import numpy as np

# Räkna medel, median, min, max för age, weight, height, systolic_bp, cholesterol
# Skapa minst 3 grafer, t.ex. histogram över blodtryck, boxplot vikt per kön, stapeldiagram för andel rökare
# VG - motivera metodval i markdown och hänvisa till dokumentation eller annan källa

# Räknar ut medel, median, min och max för valfri kolumn i datasetet
def descriptive_values(df, column):
    return {
        "mean": df[column].mean(),
        "median": df[column].median(),
        "min": df[column].min(),
        "max": df[column].max()
    }