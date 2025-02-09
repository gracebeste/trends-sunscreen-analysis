import pandas as pd
import numpy as np

# File paths for the weather data
weather_files = [
    '/Users/gracebeste/documents/trends-sunscreen-analysis/src/weather/visual-crossing/raw-data/usa_daily_weather_2020_2021.csv',
    '/Users/gracebeste/documents/trends-sunscreen-analysis/src/weather/visual-crossing/raw-data/usa_daily_weather_2022_2023.csv',
    '/Users/gracebeste/documents/trends-sunscreen-analysis/src/weather/visual-crossing/raw-data/usa_daily_weather_2024.csv'
]

# Load and concatenate all weather datasets
weather_data_list = [pd.read_csv(file) for file in weather_files]
weather_data = pd.concat(weather_data_list, ignore_index=True)

# Convert the 'date' column to datetime
weather_data['datetime'] = pd.to_datetime(weather_data['datetime'])

# Add a 'week_start' column (assuming weeks start on Sunday)
weather_data['week_start'] = weather_data['datetime'] - pd.to_timedelta(
    np.where(weather_data['datetime'].dt.weekday == 6, 0, weather_data['datetime'].dt.weekday + 1), unit='D'
)

# Aggregate to weekly level (maximum temperature per week, maximum UV index per week)
weekly_weather = weather_data.groupby('week_start').agg({
    'tempmax': 'max',
    'uvindex': 'max'
}).reset_index()

# Load Google Trends data
trends_data = pd.read_csv('/Users/gracebeste/documents/trends-sunscreen-analysis/src/sentiment/google/raw-data/usa_weekly_trends_2020_2024.csv')
trends_data['date'] = pd.to_datetime(trends_data['date'])

# Merge the datasets on 'week_start' and 'date' (Google Trends 'date' is already weekly)
merged_data = pd.merge(weekly_weather, trends_data, left_on='week_start', right_on='date')

# Save merged data
merged_data.to_csv('/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data/weather_trends_merged.csv', index=False)
print("VC Weather and Google Trends data merged and saved.")

# Conduct QC checks on merged dataset
print(weather_data.info())

weather_data.sort_values(by='datetime', inplace=True)
