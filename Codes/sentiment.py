'''
uses TextBlob to obtain sentiment for unique tweets
'''

import csv
from textblob import TextBlob
import sys

# Do some version specific stuff
if sys.version[0] == '3':
    from importlib import reload
    sntTweets = csv.writer(open("sentimentTweets.csv", "w", newline='',encoding='utf8'))

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    sntTweets = csv.writer(open("sentimentTweets.csv", "w",encoding='utf8'))

alltweets = csv.reader(open("searchTweets.csv", 'r'))

for row in alltweets:
    if(len(row)!=0): 
        blob = TextBlob(row[2])
        print (blob.sentiment.polarity)
        if blob.sentiment.polarity > 0:
            sntTweets.writerow([row[0], row[1], row[2], row[3], blob.sentiment.polarity, "positive"])
        elif blob.sentiment.polarity < 0:
            sntTweets.writerow([row[0], row[1], row[2], row[3], blob.sentiment.polarity, "negative"])
        elif blob.sentiment.polarity == 0.0:
            sntTweets.writerow([row[0], row[1], row[2], row[3], blob.sentiment.polarity, "neutral"])
        
    