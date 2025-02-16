# Plot search interest trends over time:

from data_processing import load_and_process_data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load dataset
df = load_and_process_data()

# Identify search-related columns (excluding temp/uv data)
excluded_columns = {"week_start", "tempmax", "uvindex", "month", "isPartial"}  # Adjust if needed
search_terms = [col for col in df.columns if col not in excluded_columns]

def plot_trend_over_time(term):
    """Create a line plot showing the trend of search interest over time."""
    monthly_trend = df.groupby('month')[term].mean()
    monthly_trend.index = monthly_trend.index.to_timestamp()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(monthly_trend.index, monthly_trend, color='darkblue', linewidth=2, label=term)

    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45, fontsize=8)

    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Search Interest', fontsize=12)
    plt.title(f'Monthly Search Interest for "{term}" (2020-2024)', fontsize=14)
    plt.grid(color='lightgray', linestyle='--', linewidth=0.5)

    plt.savefig(f"figures/plot-time-series/trend_{term}.png")
    plt.show()
    plt.close()

# Loop through all identified search terms dynamically
for term in search_terms:
    plot_trend_over_time(term)
