import json
import csv
# 2024
with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/raw-data/noaa_weather_data_2024.json', 'r') as json_file_2024:
    data_2024 = json.load(json_file_2024)

with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/noaa_weather_data_2024.csv', 'w', newline='') as csv_file_2024:
    writer_2024 = csv.writer(csv_file_2024)

    # WRITEROW, NEW SOLUTION
    data_rows_2024 = data_2024.get("results", [])  # Safely get the 'results' key or an empty list

    if data_rows_2024:
        writer_2024.writerow(data_rows_2024[0].keys())  # Write header row
        for row in data_rows_2024:
            writer_2024.writerow(row.values())  # Write data rows
    else:
        print("No data found under 'results'.")



# 2023
with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/raw-data/noaa_weather_data_2023.json', 'r') as json_file_2023:
    data_2023 = json.load(json_file_2023)

with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/noaa_weather_data_2023.csv', 'w', newline='') as csv_file_2023:
    writer_2023 = csv.writer(csv_file_2023)

     # WRITEROW, NEW SOLUTION
    data_rows_2023 = data_2023.get("results", [])  # Safely get the 'results' key or an empty list

    if data_rows_2023:
        writer_2023.writerow(data_rows_2023[0].keys())  # Write header row
        for row in data_rows_2023:
            writer_2023.writerow(row.values())  # Write data rows
    else:
        print("No data found under 'results'.")



# 2022
with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/raw-data/noaa_weather_data_2022.json', 'r') as json_file_2022:
    data_2022 = json.load(json_file_2022)

with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/noaa_weather_data_2022.csv', 'w', newline='') as csv_file_2022:
    writer_2022 = csv.writer(csv_file_2022)

    # WRITEROW, NEW SOLUTION
    data_rows_2022 = data_2022.get("results", [])  # Safely get the 'results' key or an empty list

    if data_rows_2022:
        writer_2022.writerow(data_rows_2022[0].keys())  # Write header row
        for row in data_rows_2022:
            writer_2022.writerow(row.values())  # Write data rows
    else:
        print("No data found under 'results'.")



# 2021
with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/raw-data/noaa_weather_data_2021.json', 'r') as json_file_2021:
    data_2021 = json.load(json_file_2021)

with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/noaa_weather_data_2021.csv', 'w', newline='') as csv_file_2021:
    writer_2021 = csv.writer(csv_file_2021)

    # WRITEROW, NEW SOLUTION
    data_rows_2021 = data_2021.get("results", [])  # Safely get the 'results' key or an empty list

    if data_rows_2021:
        writer_2021.writerow(data_rows_2021[0].keys())  # Write header row
        for row in data_rows_2021:
            writer_2021.writerow(row.values())  # Write data rows
    else:
        print("No data found under 'results'.")



# 2020
with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/raw-data/noaa_weather_data_2020.json', 'r') as json_file_2020:
    data_2020 = json.load(json_file_2020)

with open('/Users/gracebeste/Documents/trends-sunscreen-analysis/noaa_weather_data_2020.csv', 'w', newline='') as csv_file_2020:
    writer_2020 = csv.writer(csv_file_2020)

     # WRITEROW, NEW SOLUTION
    data_rows_2020 = data_2020.get("results", [])  # Safely get the 'results' key or an empty list

    if data_rows_2020:
        writer_2020.writerow(data_rows_2020[0].keys())  # Write header row
        for row in data_rows_2020:
            writer_2020.writerow(row.values())  # Write data rows
    else:
        print("No data found under 'results'.")