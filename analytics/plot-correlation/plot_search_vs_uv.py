# Creating plots comparing the patterns for different search terms with maximum temps at that time:

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the processed data
df = pd.read_csv("/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data/weather_trends_cleaned.csv", parse_dates=["week_start"])

# Creating a function plot_search_vs_temp() to loop through the different search terms and create a temp comparison plot for each term:
def plot_search_vs_temp(search_term):
    """Create scatterplot of maximum UV index values vs. search interest for a given search term."""
    if search_term not in df.columns:
        print(f"Warning: Column '{search_term}' not found in dataset.")
        return

    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='uvindex', y=search_term, data=df, alpha=0.5)
    sns.regplot(x=df["uvindex"], y=df[search_term], scatter_kws={"alpha": 0.5}, line_kws={"color": "mediumaquamarine"})

    plt.title(f'Correlation Between Max UV Index and "{search_term}" Search Interest')
    plt.xlabel('Max UV Index Value Per Week')
    plt.ylabel(f'Search Interest for "{search_term}"')

    plt.savefig(f"figures/plot-correlation/uv_vs_{search_term}.png")
    plt.show()
    plt.close()

# Generate plots for different search terms
search_terms = ["sunscreen", "SPF", "UV protection", "skincare"]

for term in search_terms:
    plot_search_vs_temp(term)
