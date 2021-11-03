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

'''#imports for additionals - xlsx to email
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders'''

#Base Code Proper
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

tweets = tweepy.Cursor(api.search_tweets,q=keyword,lang="en",since_id=0).items(1000)

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
print('Excel File has been created!')

'''#Additional: Email - Proper
#Getting variables needed to set up email 'from' and 'to'
emailSubject = 'Assignment Output'
emailSender = input("Please enter the email of the sender: ")
emailReceiver = input("Please enter the email of the receiver: ")
password = '' #input("Please enter the sender's password: ")
context=ssl.create_default_context()

#Attaching file to the email to be sent
msg = MIMEMultipart()
msg['From'] = emailSender
msg['To'] = emailReceiver
msg['Date'] = formatdate(localtime = True)
msg['Subject'] = emailSubject

part = MIMEBase('application', "octet-stream")
part.set_payload(open("test_sheet.xlsx", "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="test_sheet.xlsx"')
msg.attach(part)

#context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
#SSL connection only working on Python 3+
smtp = smtplib.SMTP('localhost')
smtp.starttls(context=context)
smtp.login('',password)
smtp.sendmail(emailSender, emailReceiver, msg.as_string())
smtp.close()'''
