from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define keywords and timeframe
keywords = ["sunscreen", "SPF", "UV protection", "skincare"]
pytrends.build_payload(keywords, cat=0, timeframe='2020-01-01 2024-12-31', geo='US', gprop='')

# Fetch interest over time
data = pytrends.interest_over_time()
data.to_csv('/Users/gracebeste/documents/trends-sunscreen-analysis/sentiment/google/raw-data/usa_weekly_trends_2020_2024.csv')
print("Google Trends sunscreen keyword trend data saved.")

# Note: using pytrends.interest_over_time() means that each date in the dataset is the starting date of the week to which the data refers.
# E.g., the row with "2019-12-29" as the date corresponds to the week: 2019-12-29 through 2020-01-04