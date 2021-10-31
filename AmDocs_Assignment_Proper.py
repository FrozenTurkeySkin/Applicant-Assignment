import sys
import tweepy
import pandas as pd
import numpy as np
import os
import re
import string
import csv
import preprocessor as p

consumerKey = 'R6GDVzcRKfQdN89iJa1aYC1il'
consumerSecret = 'IT0CcISarLGiuC8JxI9SVYObB7BLTkOP3zSDKSTkAdodaYud8y'
accessToken = '1366193316753076224-dQMTKaMhLixAt8xwitg6l8Fn9VRFNn'
accessTokenSecret = 'wYXOIkXMkcHkdOepG43Xl91sWvMo0VWx3NucGrGfvX5Mv'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

funny_list = []
unfunny_list = []

#Getting the tweets for sorting
keyword = input("Please enter keyword or hashtag to search: ") + " -filter:retweets"

tweets = tweepy.Cursor(api.search_tweets,q=keyword,lang="en",since_id=0).items(10)

for tweet in tweets:
    testString = tweet.text
    if 'funny' in testString:
        funny_list.append(testString)
    else:
        unfunny_list.append(testString)

funny_list = pd.DataFrame(funny_list)
unfunny_list = pd.DataFrame(unfunny_list)

sheetWriter = pd.ExcelWriter('test_sheet.xlsx', engine = 'xlsxwriter')

funny_list.to_excel(sheetWriter, sheet_name='Funny Tweets List')
unfunny_list.to_excel(sheetWriter, sheet_name='Unfunny Tweets List')

sheetWriter.save()
