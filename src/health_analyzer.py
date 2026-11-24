import pandas as pd

class HealthAnalyzer:
    """Class analyzing health data"""
    
    def __init__(self, df):
        self.df = df

    def health_stats(self, column):
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