# Plot trend lines over time
def plot_trend_over_time(search_term):
    """Create a line plot showing the trend of search interest over time."""
    if search_term not in df.columns:
        print(f"Warning: Column '{search_term}' not found in dataset.")
        return
    
    monthly_trend = df.groupby('month')[search_term].mean()
    monthly_trend.index = monthly_trend.index.to_timestamp()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(monthly_trend.index, monthly_trend, color='darkblue', linewidth=2, label=search_term)
    
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45, fontsize=8)
    
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Search Interest', fontsize=12)
    plt.title(f'Monthly Search Interest for "{search_term}" (2020-2024)', fontsize=14)
    plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
    
    plt.savefig(f"figures/trend_{search_term}.png")
    plt.show()
    plt.close()

for term in search_terms:
    plot_trend_over_time(term)
