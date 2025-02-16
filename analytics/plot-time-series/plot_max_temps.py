# Creating a plot with maximum monthly temperatures from 2020-2024:

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data/weather_trends_cleaned.csv")

# Ensure 'week_start' is a datetime type
df['week_start'] = pd.to_datetime(df['week_start'])

# Set 'week_start' as the index
df.set_index('week_start', inplace=True)

# Compute monthly max temperature
# monthly_max_temp = df.groupby('month')['tempmax'].max()
# monthly_max_temp.index = monthly_max_temp.index.to_timestamp()

def plot_temp_over_time():
    """Create a line plot showing the maximum temperatures over time."""

     # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['tempmax'], color='darkmagenta', linewidth=2, label='Max Temp')

    # Format axes
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45, fontsize=8)

    # Labeling axes, creating title, and formatting background of plot
    plt.xlabel('Month', fontsize=12) # The labels are the months for visualization purposes, even though the data included is at a weekly level
    plt.ylabel('Temperature (°F)', fontsize=12)
    plt.title('Weekly Maximum Temperatures (2020-2024)', fontsize=14)
    plt.grid(color='blanchedalmond', linestyle='--', linewidth=0.5)

    # Save & show
    plt.savefig("figures/plot-time-series/weekly_max_temp.png")
    plt.show()

plot_temp_over_time()