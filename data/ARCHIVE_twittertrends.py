import tweepy
import json

# Twitter API keys
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search tweets
query = "#sunscreen OR #SPF OR #UVprotection OR #skincare"
tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", since="2013-01-01").items(1000)

# Save tweets to JSON
tweets_data = [{"text": tweet.text, "created_at": tweet.created_at} for tweet in tweets]
with open('/Users/gracebeste/documents/trends-sunscreen-analysis/tweets_sunscreen.json', 'w') as file:
    json.dump(tweets_data, file)
print("Twitter sunscreen trend data saved.")
