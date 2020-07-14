'''
Authenticate and connect with Twitter
Use the search REST API to gather tweets from a list of keywords
Store tweets as a csv file
'''
import tweepy
import sys
import csv

# import twitter keys and tokens
from credentials import *

# Do some version specific stuff
if sys.version[0] == '3':
    from importlib import reload

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

#Create a new file to hold the results
alltweets = csv.writer(open("searchTweets.csv", 'w'))

def search(keywords):

    # Authenticate using your Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    keyword = keywords.strip(' \t\n\r')

    count = 1;
    for tweet in tweepy.Cursor(api.search,q=keyword).items(200): 
        created_at =  tweet.created_at  # accessing tweet time
        tweet_id = tweet.id_str         # accessing tweet id
        tweet_text = tweet.text.encode("utf-8")         # accessing tweet text
        print ("collected tweet " + str(count))
        count = count + 1
        alltweets.writerow([created_at, tweet_id, tweet_text, keyword])

file = open('keywords.txt', 'r') # contains a list of keywords
queries = file.readlines()

for q in queries:
    # read one keyword at a time
    print ("----")
    print (q)
    search(q)