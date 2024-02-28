import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
OVERWEIGHT_THRESHOLD = 25

bmi = df["weight"] / (df["height"] / 100) ** 2
df["overweight"] = (bmi > OVERWEIGHT_THRESHOLD).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df[["cholesterol", "gluc"]] = (df[["cholesterol", "gluc"]] > 1).astype(int)

df.groupby()


# Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["active", "cholesterol", "gluc", "overweight", "smoke"],
    )
    df_cat["total"] = 0
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).count()

    fig = sns.catplot(
        data=df_cat, x="variable", y="total", col="cardio", kind="bar", hue="value"
    )

    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None

    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'

    # Do not modify the next two lines
    fig.savefig("heatmap.png")
    return fig
