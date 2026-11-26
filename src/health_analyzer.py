import pandas as pd

class HealthAnalyzer:
    """Class analyzing health data"""
    
    def __init__(self, df):
        self.df = df
        smoker_compare = self.df["smoker"]

        smokers = self.df.loc[
            smoker_compare == "Yes", "systolic_bp"
        ]
        
        non_smokers = self.df.loc[
            smoker_compare == "No", "systolic_bp"
        ]

    def health_stats(self):
        """Descriptive stats for a chosen column"""

        columns = ["age", "weight", "height", "systolic_bp", "cholesterol"]

        results = {}

        for column in columns:
            values = self.df[column]
            results[column] = {
                "mean": values.mean(),
                "median": values.median(),
                "min": values.min(),
                "max": values.max()
            }

        return pd.DataFrame(results).T

    def compare_bp(self):
        """Compare mean blood preassure between smokers and non-smokers"""

        return {
            "smokers": self.smokers.mean(),
            "non_smokers": self.non_smokers.mean()
        }