import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data
merged_data = pd.read_csv('/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/weather_trends_merged.csv')
'''
# Convert 'week_start' to datetime and create 'month' column
merged_data['week_start'] = pd.to_datetime(merged_data['week_start'])
merged_data['month'] = merged_data['week_start'].dt.to_period('M')

# Group by month and get the max temperature for each month
monthly_max_temp = merged_data.groupby('month')['tempmax'].max()

# Convert PeriodIndex to DatetimeIndex (first day of each month)
monthly_max_temp.index = monthly_max_temp.index.to_timestamp()

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axis for better control

# Plot the monthly max temperature
ax.plot(monthly_max_temp.index, monthly_max_temp, color='darkmagenta', linewidth=2, label='Max Temp')

# Set major locator to place a tick for each month
ax.xaxis.set_major_locator(mdates.MonthLocator())

# Set the format for the x-axis labels to display "Month Year"
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, fontsize=8)

# Customize Y-axis to show increments of 5 (based on the range of temperatures)
min_temp = monthly_max_temp.min()
max_temp = monthly_max_temp.max()
plt.yticks(range(int(min_temp) - 5, int(max_temp) + 5, 5), fontsize=10)

# Add labels and title
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)
plt.title('Monthly Maximum Temperatures (2020-2024)', fontsize=14)

# Add grid for better readability
plt.grid(color='blanchedalmond', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()


# List available colors for customization
available_colors = list(mcolors.CSS4_COLORS.keys())
print("Available colors:", available_colors)
'''

import seaborn as sns

# Example: Correlation between temperature and search interest
# merged_data = pd.merge(weather_data, trends_data, on='date')

# Creating a scatterplot for "Sunscreen" searches
sns.scatterplot(x='tempmax', y='sunscreen', data=merged_data)
sns.regplot(x=merged_data["tempmax"], y=merged_data["sunscreen"], scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.title('Correlation Between Temperature and "Sunscreen" Search Interest')
plt.xlabel('Max Temperature Per Week (°F)')
plt.ylabel('Search Interest for "Sunscreen"')
plt.show()
'''
# Creating a scatterplot for "SPF" searches
sns.scatterplot(x='tempmax', y='sunscreen', data=merged_data)
plt.title('Correlation Between Temperature and "Sunscreen" Search Interest')
plt.xlabel('Max Temperature Per Week (°F)')
plt.ylabel('Search Interest for "Sunscreen"')
plt.show()

# Creating a scatterplot for "UV Protection" searches
sns.scatterplot(x='tempmax', y='sunscreen', data=merged_data)
plt.title('Correlation Between Temperature and "Sunscreen" Search Interest')
plt.xlabel('Max Temperature Per Week (°F)')
plt.ylabel('Search Interest for "Sunscreen"')
plt.show()

# Creating a scatterplot for "skincare" searches
sns.scatterplot(x='tempmax', y='sunscreen', data=merged_data)
plt.title('Correlation Between Temperature and "Sunscreen" Search Interest')
plt.xlabel('Max Temperature Per Week (°F)')
plt.ylabel('Search Interest for "Sunscreen"')
plt.show()
'''