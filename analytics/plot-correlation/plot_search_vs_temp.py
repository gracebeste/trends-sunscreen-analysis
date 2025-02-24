# Create plots comparing search term interest with maximum temps

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and read in the processed data
df = pd.read_csv("/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data-cleaning/data/weather_trends_cleaned.csv", parse_dates=["week_start"])

# Create a function plot_search_vs_temp() to loop through the different search terms and create a temp comparison plot for each term:
def plot_search_vs_temp(search_term):
    """Create scatterplot of maximum temperatures vs. search interest for a given search term."""

    # Error handling to ensure plot only graphs search term columns
    if search_term not in df.columns:
        print(f"Warning: Column '{search_term}' not found in dataset.")
        return

    # Create plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='tempmax', y=search_term, data=df, alpha=0.5)
    sns.regplot(x=df["tempmax"], y=df[search_term], scatter_kws={"alpha": 0.5}, line_kws={"color": "mediumaquamarine"})

    # Adjust plot titles
    plt.title(f'Correlation Between Temperature and "{search_term}" Search Interest')
    plt.xlabel('Max Temperature Per Week (°F)')
    plt.ylabel(f'Search Interest for "{search_term}"')

    # Save the file and ensure there are no spaces in the file name
    filename = f"figures/plot-correlation/temp_vs_{term.replace(' ', '_')}.png"
    plt.savefig(filename, bbox_inches='tight')
    plt.show()
    plt.close()

# Loop through search terms to generate different plots
search_terms = ["sunscreen", "SPF", "UV protection", "skincare"]
for term in search_terms:
    plot_search_vs_temp(term)
