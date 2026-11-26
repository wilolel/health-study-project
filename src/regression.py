from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def linear_regression(df):
    """Linear regression using blood pressure and age"""

    X = df[["age"]]
    y = df["systolic_bp"].to_numpy()

    model = LinearRegression()
    model.fit(X, y)

    print("Skärning:", model.intercept_)
    print("Lutning:", model.coef_[0])
    print("R2:", model.score(X, y))

    x_line = pd.DataFrame({
        "age": np.linspace(X["age"].min(), X["age"].max(), 100)
    })

    fig, ax = plt.subplots(figsize=(9,6))

    ax.scatter(
        X["age"],
        y,
        alpha=0.6,
        label="Observationer"
    )

    ax.plot(
        x_line["age"],
        model.predict(x_line),
        color="red",
        label="Regressionslinje"
    )

    ax.set(
        title="Linjär regression - ålder och blodtryck",
        xlabel="Ålder",
        ylabel="Blodtryck"
    )

    ax.legend()
    ax.grid(True, alpha=0.5)

    plt.tight_layout()
    plt.show()