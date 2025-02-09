# Creating a plot with maximum monthly temperatures from 2020-2024:

from data_processing import load_and_process_data
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = load_and_process_data()

# Compute monthly max temperature
monthly_max_temp = df.groupby('month')['tempmax'].max()
monthly_max_temp.index = monthly_max_temp.index.to_timestamp()

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(monthly_max_temp.index, monthly_max_temp, color='darkmagenta', linewidth=2, label='Max Temp')

# Format axes
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45, fontsize=8)

# Labeling axes, creating title, and formatting background of plot
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)
plt.title('Monthly Maximum Temperatures (2020-2024)', fontsize=14)
plt.grid(color='blanchedalmond', linestyle='--', linewidth=0.5)

# Save & show
plt.savefig("figures/monthly_max_temp.png")
plt.show()