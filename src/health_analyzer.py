import pandas as pd
import matplotlib.pyplot as plt

class HealthAnalyzer:
    """Class analyzing health data"""
    
    def __init__(self, df):
        """Initializing health analyzer with health data and blood pressure groups"""
        
        self.df = df
        smoker_compare = self.df["smoker"]

        self.smokers_bp = self.df.loc[
            smoker_compare == "Yes", "systolic_bp"
        ]
        
        self.non_smokers_bp = self.df.loc[
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
            "smokers_bp": self.smokers_bp.mean(),
            "non_smokers_bp": self.non_smokers_bp.mean()
        }

    def boxplot_bp(self):
        """Boxplot - blood pressure distribution between smokers and non-smokers"""

        fig, ax = plt.subplots(figsize=(9,6))

        box = ax.boxplot([self.smokers_bp, self.non_smokers_bp], tick_labels=["Smokers", "Non-smokers"], patch_artist=True)
        box["boxes"][0].set_facecolor("tab:blue")
        box["boxes"][1].set_facecolor("tab:green")

        ax.set_title("Smokers and non-smokers - Bloodpressure distribution")
        ax.set_ylabel("Systolic blood pressure")
        ax.grid(True, axis="y", alpha=0.3)

        plt.tight_layout()
        plt.show()