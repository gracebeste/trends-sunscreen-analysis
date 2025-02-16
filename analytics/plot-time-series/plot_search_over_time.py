# Plot search interest trends over time:

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load cleaned dataset
df = pd.read_csv("/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data/weather_trends_cleaned.csv", parse_dates=["week_start"])

# Set 'week_start' as the index
df.set_index('week_start', inplace=True)

# Identify search-related columns
excluded_columns = {"week_start", "tempmax", "uvindex"} 
search_terms = [col for col in df.columns if col not in excluded_columns]

def plot_trend_over_time(term):
    """Create a line plot showing the trend of search interest over time."""

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df[term], color='darkblue', linewidth=2, label=term)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45, fontsize=8)

    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Search Interest', fontsize=12)
    plt.title(f'Search Interest for "{term}" (2020-2024)', fontsize=14)
    plt.grid(color='lightgray', linestyle='--', linewidth=0.5)

    plt.savefig(f"figures/plot-time-series/trend_{term}.png")
    plt.show()
    plt.close()

# Loop through all identified search terms dynamically
for term in search_terms:
    plot_trend_over_time(term)
