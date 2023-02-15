#this will contain our custom definition of tweet
#we need to have functions that will remove garbage from the tweet
class CustomTweet:
    text = "" #whatever the content of tweet is
    wordCount = 0 #we need to know how long this tweet is
    trend = "" #we need to know what trend this tweet is related to
    
    def tokensCount(self):
        self.text.split("")

class TrendsAndTweets:
    city = ""
    trends = []
    tweets = []