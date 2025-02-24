# Creating a function load_and_process_data() to clean the merged dataset. 

import pandas as pd

def load_and_process_data():
    """Load the dataset, preprocess columns, and save cleaned weekly data."""
    
    # Load raw data
    filepath = "/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data-cleaning/data/weather_trends_merged.csv"
    df = pd.read_csv(filepath)

    # Convert 'week_start' to datetime (force proper format)
    df["week_start"] = pd.to_datetime(df["week_start"], format="%Y-%m-%d", errors="coerce")

    # Exclude "date" and "isPartial" from the cleaned dataset
    df = df.drop(columns=["date", "isPartial"], errors="ignore")

    # Define columns to include in numeric data type conversion
    excluded_columns = {"week_start"}  
    numeric_columns = [col for col in df.columns if col not in excluded_columns]

    # Convert columns to numeric data types (force errors to NaN)
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

    # Save cleaned dataset
    save_path = "/Users/gracebeste/documents/trends-sunscreen-analysis/analytics/data-cleaning/data/weather_trends_cleaned.csv"
    df.to_csv(save_path, index=False)

    print(f"Processed dataset saved to: {save_path}")

    return df

load_and_process_data()