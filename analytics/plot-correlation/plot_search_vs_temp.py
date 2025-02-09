# Creating plots comparing the patterns for different search terms with maximum temps at that time:

import matplotlib.pyplot as plt
import seaborn as sns
from data_processing import load_and_process_data

# Load the processed data
df = load_and_process_data()

# Creating a function plot_search_vs_temp() to loop through the different search terms and create a temp comparison plot for each term:
def plot_search_vs_temp(search_term):
    """Create scatterplot of maximum temperatures vs. search interest for a given search term."""
    if search_term not in df.columns:
        print(f"Warning: Column '{search_term}' not found in dataset.")
        return

    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='tempmax', y=search_term, data=df, alpha=0.5)
    sns.regplot(x=df["tempmax"], y=df[search_term], scatter_kws={"alpha": 0.5}, line_kws={"color": "mediumaquamarine"})

    plt.title(f'Correlation Between Temperature and "{search_term}" Search Interest')
    plt.xlabel('Max Temperature Per Week (°F)')
    plt.ylabel(f'Search Interest for "{search_term}"')

    plt.savefig(f"figures/temp_vs_{search_term}.png")
    plt.show()
    plt.close()

# Generate plots for different search terms
search_terms = ["sunscreen", "SPF", "UV protection", "skincare"]

for term in search_terms:
    plot_search_vs_temp(term)
