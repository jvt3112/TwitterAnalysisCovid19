import tweepy
import csv
from tokens import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# Open/Create a file to append data
csvFile = open('./mydata/test.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Pfizer",count=100,
                           lang="en",
                           since="2021-05-11",tweet_mode='extended').items():
    csvWriter.writerow([tweet.full_text.encode('utf-8'),tweet.retweet_count,tweet.user.followers_count,tweet.favorite_count,tweet.place,tweet.coordinates,tweet.geo,tweet.created_at])
print('Done!')