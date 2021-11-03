#imports for base assignment
import sys
import tweepy
import pandas as pd
import numpy as np
import os
import re
import string
import csv
import preprocessor as p

#Base Code Proper
#Set environ variables for API keys
os.environ['CONKEY'] = 'R6GDVzcRKfQdN89iJa1aYC1il'
os.environ['CONKEYSEC'] = 'IT0CcISarLGiuC8JxI9SVYObB7BLTkOP3zSDKSTkAdodaYud8y'
os.environ['ACCTOK'] = '1366193316753076224-dQMTKaMhLixAt8xwitg6l8Fn9VRFNn'
os.environ['ACCTOKSEC'] = 'wYXOIkXMkcHkdOepG43Xl91sWvMo0VWx3NucGrGfvX5Mv'

def writeTweetToExcel(funnyList, unfunnyList):
    #Store data gathered (and sorted) as a dataframe to their respective lists
    funny_list = pd.DataFrame(funnyList)
    unfunny_list = pd.DataFrame(unfunnyList)

    #Code to write data into excel sheet
    sheetWriter = pd.ExcelWriter('test_sheet.xlsx', engine = 'xlsxwriter')

    funny_list.to_excel(sheetWriter, sheet_name='Funny Tweets List')
    unfunny_list.to_excel(sheetWriter, sheet_name='Unfunny Tweets List')

    sheetWriter.save()
    print('Excel File has been created! Program is now closing.')

def tweetSearch(keyword, api):
    #Lists where tweets will be sorted and stored (and later saved as separate sheets in an excel file)
    funnyList = []
    unfunnyList = []
    tweets = tweepy.Cursor(api.search_tweets,q=keyword,lang="en",since_id=0).items(1000)
    for tweet in tweets:
        testString = tweet.text
        if 'funny' in testString:
            funnyList.append(testString)
        else:
            unfunnyList.append(testString)

    writeTweetToExcel(funnyList, unfunnyList)

def inputChecker(inputGiven):
    stringToTest = inputGiven
    if not stringToTest or re.search("^\s*$", stringToTest):
        print('String is either empty or Blank or contain only spaces')
        #Authenticate access to Twitter API using Dev Account API keys
        auth = tweepy.OAuthHandler(os.environ.get('CONKEY'), os.environ.get('CONKEYSEC'))
        auth.set_access_token(os.environ.get('ACCTOK'), os.environ.get('ACCTOKSEC'))
        api = tweepy.API(auth)
        tweetSearch(stringToTest, api)
    else:
        print('Input is not valid to be used for searching. Program will now close.')

#Getting the tweets for sorting
keyword = input("Please enter keyword or hashtag to search: ") + " -filter:retweets"
inputChecker(keyword)
