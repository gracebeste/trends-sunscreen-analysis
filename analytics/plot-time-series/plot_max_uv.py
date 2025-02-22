# Create a plot with maximum weekly UV index values from 2020-2024:

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read in dataset:
df = pd.read_csv("/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data/weather_trends_cleaned.csv", parse_dates=["week_start"])

# Set 'week_start' as the index
df.set_index('week_start', inplace=True)

# Extract year and month for color-coding
df['year'] = df.index.year
df['month'] = df.index.strftime('%b')  # Abbreviated month names (Jan, Feb, etc.)

# Assign unique colors to each year (for the x-axis tick mark labels)
import seaborn as sns
years = sorted(df['year'].unique())  
year_colors = sns.color_palette("husl", len(years))  # Generates distinct colors
year_color_map = {year: color for year, color in zip(years, year_colors)}

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df.index, df['uvindex'], color='chocolate', linewidth=2, label='Max UV')

# Format axes
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b')) # Only show month names

# Modify tick labels to color-code them by year
tick_labels = [tick.get_text() for tick in ax.get_xticklabels()]
tick_dates = [mdates.num2date(tick) for tick in ax.get_xticks()]  # Convert tick positions to dates

for label, tick_date in zip(ax.get_xticklabels(), tick_dates):
    year = tick_date.year
    label.set_color(year_color_map.get(year, 'black'))  # Assign color based on year

# Adjust label visibility
plt.xticks(rotation=45, fontsize=7.5)
plt.subplots_adjust(bottom=0.15)  # Avoid cutoff issues for x-axis title

# Label axes, create title, and format the background of the plot
plt.xlabel('Month', fontsize=12)  # The labels are the months for visualization purposes, even though the data is at a weekly level
plt.ylabel('UV Index Values', fontsize=12)
plt.title('Weekly Maximum UV Index Values (2020-2024)', fontsize=14)
plt.grid(color='blanchedalmond', linestyle='--', linewidth=0.5)

# Add a legend to show which colors represent which years
legend_patches = [plt.Line2D([0], [0], color=color, lw=4, label=str(year)) for year, color in year_color_map.items()]
plt.legend(handles=legend_patches, title="Year", fontsize=10, loc="upper left")

# Save & show
plt.savefig("figures/plot-time-series/weekly_max_uv.png")
plt.show()