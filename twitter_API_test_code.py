import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
consumer_key = 'R6GDVzcRKfQdN89iJa1aYC1il'
consumer_secret = 'IT0CcISarLGiuC8JxI9SVYObB7BLTkOP3zSDKSTkAdodaYud8y'
access_key= '1366193316753076224-dQMTKaMhLixAt8xwitg6l8Fn9VRFNn'
access_secret = 'wYXOIkXMkcHkdOepG43Xl91sWvMo0VWx3NucGrGfvX5Mv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

search_words = "#mitsubishi"      #enter your words
new_search = search_words + " -filter:retweets"

for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=100,
                           lang="en",
                           since_id=0).items():
    csvFile = open('test_file.csv', 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


