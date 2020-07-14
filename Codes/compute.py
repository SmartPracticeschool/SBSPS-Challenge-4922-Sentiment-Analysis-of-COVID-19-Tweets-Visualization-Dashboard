'''
compute total, positive, negative and neutral tweets for each keyword
'''

import csv

def getStats(keyword):
    tot = 0;
    pos = 0;
    neg = 0;
    neu = 0;

    fileRead = csv.reader(open(keyword + "Tweets.csv", "r"))
    for row in fileRead:
        tot = tot + 1;
        if row[5] == "positive":
            pos = pos + 1;
        elif row[5] == "negative":
            neg = neg + 1;
        elif row[5] == "neutral":
            neu = neu + 1;
    print ("Tweets Stats for" + str(keyword))
    print ("total tweets: " + str(tot))
    print ("positive: " + str(pos))
    print ("negative: " + str(neg))
    print ("neutral: " + str(neu))
    results.writerow([keyword, tot, pos, neg, neu])

results = csv.writer(open("Final.csv", "w"))

keywords = open('keywords.txt', 'r') # contains a list of keywords

queries = keywords.readlines()

for q in queries:
    q = q.strip(' \t\n\r')
    print (q)
    getStats(q)