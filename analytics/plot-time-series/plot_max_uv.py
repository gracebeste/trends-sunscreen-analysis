# Creating a plot with maximum monthly temperatures from 2020-2024:

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data/weather_trends_cleaned.csv")

def plot_uv_over_time():
    """Create a line plot showing the maximum UV index values over time."""
    # Compute monthly max UV index
  #  monthly_max_uv = df.groupby('month')['uvindex'].max()
  #  monthly_max_uv.index = monthly_max_uv.index.to_timestamp()

    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['uvindex'].index, df['uvindex'], color='chocolate', linewidth=2, label='Max UV')

    # Format axes
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45, fontsize=8)

    # Labeling axes, creating title, and formatting background of plot
    plt.xlabel('Month', fontsize=12)  # The labels are the months for visualization purposes, even though the data included is at a weekly level
    plt.ylabel('UV Index Values', fontsize=12)
    plt.title('Weekly Maximum UV Index Values (2020-2024)', fontsize=14)
    plt.grid(color='blanchedalmond', linestyle='--', linewidth=0.5)

    # Save & show
    plt.savefig("figures/weekly_max_uv.png")
    plt.show()

    # List available colors for customization
    import matplotlib.colors as mcolors
    available_colors = list(mcolors.CSS4_COLORS.keys())
    print("Available colors:", available_colors)

plot_uv_over_time()