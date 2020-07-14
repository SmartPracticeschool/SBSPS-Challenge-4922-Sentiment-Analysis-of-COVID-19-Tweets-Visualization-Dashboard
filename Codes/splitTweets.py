'''
splits and stores tweets by keyword
'''
import sys
import csv

def splitTweets(keyword):
    # create a file for each keyword
    if sys.version[0] == '3':
       keywordTweet = csv.writer(open(keyword+"Tweets.csv", "w", newline='',encoding='utf8'))

    if sys.version[0] == '2':
       keywordTweet = csv.writer(open(+keyword+"Tweets.csv", "w",encoding='utf8'))

    # open the sentiment results file
    sntTweets = csv.reader(open("sentimentTweets.csv", 'r',encoding='utf8'))
    # store tweets by keyword
    count = 0
    
    for row in sntTweets:
        r = row[2].lower()
        r = row[2].strip('#').strip('@')
        if keyword in r:
            count = count + 1
            keywordTweet.writerow(row)
    print ("Number of rows" + str(count))

keywords = open('keywords.txt', 'r') # contains a list of keywords

queries = keywords.readlines()

for q in queries:
    q = q.strip(' \t\n\r')
    print (q)
    splitTweets(q)