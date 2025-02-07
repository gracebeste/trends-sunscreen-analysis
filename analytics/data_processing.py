# Creating a function load_and_process_data() to do the same data processing for each plot script:

import pandas as pd

def load_and_process_data():
    """Load the dataset and apply necessary 'week_start' and 'month' transformations."""
    filepath = "/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data/weather_trends_merged.csv"
    
    df = pd.read_csv(filepath)
    df['week_start'] = pd.to_datetime(df['week_start'])
    df['month'] = df['week_start'].dt.to_period('M')

    return df