# Note: For the VC Weather API scripts, these are broken down into 3 separate scripts, 
# due to VC Weather API's download restrictions for free accounts, which limit
# users to scrape only 1,000 rows of data per day.

# Loading relevant libraries
import requests
from dotenv import load_dotenv
import os

# Obtaining unique API key from .env file
load_dotenv(dotenv_path="/Users/gracebeste/Documents/trends-sunscreen-analysis/api-keys.env")
VC_API_KEY = os.getenv("VC_API_KEY")

# Print statement to confirm that the .env file is properly working and accessible by the script
print(f"Loaded API Key: {VC_API_KEY}")

# Base URL incorporating unique API key
base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/USA/2022-01-01/2023-12-31?key={VC_API_KEY}"

# Parameters for the API query
params = {
    "unitGroup": "us",  # Fahrenheit
    "key": VC_API_KEY, #My API key
    "contentType": "csv",  # CSV format
    "include": "days",  # Daily temperature data
    "startDateTime": "2022-01-01", # Starting in 2022
    "endDateTime": "2023-12-31" # Ending in 2023 --> VC's row count limit is 1000/day, so I'm downloading 2 years maximum per dataset
}

# Make the API request
response = requests.get(base_url, params=params)

# Check for successful response
if response.status_code == 200:
    # Save data to a CSV file
    with open("/Users/gracebeste/Documents/trends-sunscreen-analysis/weather/visual-crossing/raw-data/usa_daily_weather_2022_2023.csv", "wb") as file:
        file.write(response.content)
    print("Data saved to 'usa_daily_weather_2022_2023.csv'")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
