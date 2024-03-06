import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")

OVERWEIGHT_THRESHOLD = 25

bmi = df["weight"] / (df["height"] / 100) ** 2
df["overweight"] = (bmi > OVERWEIGHT_THRESHOLD).astype(int)

df[["cholesterol", "gluc"]] = (df[["cholesterol", "gluc"]] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["active", "alco", "cholesterol", "gluc", "smoke", "overweight"],
    )
    df_cat["total"] = 0
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).count()

    fig = sns.catplot(
        data=df_cat, x="variable", y="total", col="cardio", kind="bar", hue="value"
    ).fig

    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr(method="pearson")

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        corr,
        linewidths=1,
        annot=True,
        square=True,
        fmt=".1f",
        center=0.08,
        cbar_kws={"shrink": 0.5},
        ax=ax,
        mask=mask,
    )

    # Do not modify the next two lines
    fig.savefig("heatmap.png")
    return fig
