# Building overlay plots comparing the individual effects of temperature or UV index values against search terms

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed data
df = pd.read_csv("/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data/weather_trends_cleaned.csv", parse_dates=["week_start"])

# Normalize tempmax and uvindex to a 0-1 scale, to make them comparable in one overlay plot:
df["tempmax_norm"] = (df["tempmax"] - df["tempmax"].min()) / (df["tempmax"].max() - df["tempmax"].min())
df["uvindex_norm"] = (df["uvindex"] - df["uvindex"].min()) / (df["uvindex"].max() - df["uvindex"].min())

def plot_normalized_correlation(search_term):
    """Create scatter plots of temperature & UV index vs. search interest, with best-fit lines."""
    if search_term not in df.columns:
        print(f"Warning: Column '{search_term}' not found in dataset.")
        return

    plt.figure(figsize=(8, 5))

    # Scatter + Regression for Normalized Temperature
    sns.scatterplot(x=df["tempmax_norm"], y=df[search_term], alpha=0.5, label="Temperature", color="crimson")
    sns.regplot(x=df["tempmax_norm"], y=df[search_term], scatter=False, line_kws={"color": "crimson", "label": "Temp Trend"})

    # Scatter + Regression for Normalized UV Index
    sns.scatterplot(x=df["uvindex_norm"], y=df[search_term], alpha=0.5, label="UV Index", color="royalblue")
    sns.regplot(x=df["uvindex_norm"], y=df[search_term], scatter=False, line_kws={"color": "royalblue", "label": "UV Trend"})

    # Titles & Labels
    plt.title(f'Normalized Correlation: Temp & UV vs. "{search_term}" Search Interest')
    plt.xlabel('Normalized Temperature & UV Index (0-1 Scale)')
    plt.ylabel(f'Search Interest for "{search_term}"')

    # Save & Show
    plt.legend()
    plt.savefig(f"figures/plot-correlation/normalized_temp_uv_vs_{search_term}.png")
    plt.show()
    plt.close()

# Generate plots for different search terms
search_terms = ["sunscreen", "SPF", "UV protection", "skincare"]

for term in search_terms:
    plot_normalized_correlation(term)