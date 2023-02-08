'''
Just want to write a custom service class that will act as mask to connect to twitter api
'''

import tweepy
import threading


class TwitterService:
    # Your Twitter API credentials, we need to move these to some kind of secret
    consumer_key = 'xNMbL8Oqd4L0FkpJZa7afNzDB'
    consumer_secret = 'RsFQo5GugF09yi70px9tpSKytjXoPveHM8WTi4oom2ZgQEmP1r'
    access_token = '1052156414-mBsC0d3w5nNNma2tGlF3kyQnwTUmiHox5vqzsSM'
    access_token_secret = '3dFbquLNNYtwGFfdHWunv1TdAMxyzGgMz75wYgfmjUUdH'
    # Authenticate your API credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Initialize the API client
    api = tweepy.API(auth)
    trendsAndTweets = []
    trends = []

    # Function to get the top 20 tweets for a trend
    def get_tweets(self, trends, tweets):
        for trend in trends[0]["trends"]:
            currentTweets = self.api.search_tweets(q=trend["name"], lang = 'en', count=5, tweet_mode="extended")
            cTweet = [tweet.full_text for tweet in currentTweets]
            tweets.extend(cTweet)

    def connectToTwitter(self):
        try:
            self.api.verify_credentials()
            print('Successful Authentication')
        except:
            print('Failed authentication')

    
    #There is possibility of getting 404 from twitter api.. or other errors obviously
    def getAllTrends(self):
        allIds = WOEIDMAP().all_woeid
         # Get the current trends for USA and Australia
        threads = []
        for woeid in allIds.values():
            #lets get the trends
            self.trends.append(self.api.get_place_trends(woeid))

        return self.trends
            

    def getTweets(self):
        # Create two threads to get the tweets for USA and Australia
        tweets = []
        threads = []

        for trend in self.trends:
            threads.append(threading.Thread(target=self.get_tweets, args=(trend, tweets)))

        # Start the threads
        for thread in threads:
            thread.start()

        # Wait for the threads to finish
        for thread in threads:
            thread.join()

        return tweets
    

class WOEIDMAP:
    australia_woeid = {
        # "Sydney": 1105779,
        # "Melbourne": 1103816,
        # "Brisbane": 1100968,
        # "Adelaide": 1095777,
        # "Perth": 1098081,
    }

    usa_woeid = {
        "New York": 2459115,
        # "Los Angeles": 2442047,
        # "Chicago": 2379574,
        # "Houston": 2424766,
        # "Miami": 2450022,
    }

    all_woeid = {**australia_woeid, **usa_woeid}

