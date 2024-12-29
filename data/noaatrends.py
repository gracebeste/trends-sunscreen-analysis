import requests

# NOAA API details
base_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"
headers = {"token": "YOUR_NOAA_API_TOKEN"}

# Parameters
params = {
    "datasetid": "GHCND",  # Global Historical Climatology Network Daily
    "locationid": "FIPS:US",  # US
    "startdate": "2013-01-01", # Timeframe start
    "enddate": "2024-12-28", # Timeframe end
    "datatypeid": "TMAX",  # Max temperature as an example
    "units": "metric", 
    "limit": 1000
}

# API Request
response = requests.get(base_url, headers=headers, params=params)
if response.status_code == 200:
    data = response.json()
    with open('noaa_weather_data.json', 'w') as file:
        json.dump(data, file)
    print("NOAA data saved.")
else:
    print(f"Error: {response.status_code}")
