# Creating a plot with maximum weekly UV index values from 2020-2024:

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data/weather_trends_cleaned.csv", parse_dates=["week_start"])

# Set 'week_start' as the index
df.set_index('week_start', inplace=True)

def plot_uv_over_time():
    """Create a line plot showing the maximum UV index values over time."""

    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['uvindex'], color='chocolate', linewidth=2, label='Max UV')

    # Format axes
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45, fontsize=8)

    # Labeling axes, creating title, and formatting background of plot
    plt.xlabel('Month', fontsize=12)  # The labels are the months for visualization purposes, even though the data is at a weekly level
    plt.ylabel('UV Index Values', fontsize=12)
    plt.title('Weekly Maximum UV Index Values (2020-2024)', fontsize=14)
    plt.grid(color='blanchedalmond', linestyle='--', linewidth=0.5)

    # Save & show
    plt.savefig("figures/plot-time-series/weekly_max_uv.png")
    plt.show()

plot_uv_over_time()