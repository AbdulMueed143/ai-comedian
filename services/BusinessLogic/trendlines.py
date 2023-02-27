from models.tweet import Trendline, TrendlineItem
from services.utils import CleanTweets
from services.openai import Comedian

class TrendLineManipulation:
    def __init__(self) -> None:
        pass

    #This method expects tweets of specific trend only
    def createTrendLineFromTweets(self, tweets):
        ckLouis = Comedian("CK Louis")
        prompt = ckLouis.createPromptForJoke(tweets)
        trendline = Trendline()

        for tweet in tweets:
            trendlineItem = TrendlineItem(tweet, prompt)
            trendline.addTrendline(trendlineItem)

        return trendline
    
    def getTweetsByTrend(self, tweets):
        tweetsByTrend = {}
        for tweet in tweets:
            if tweet.trend in tweetsByTrend:
                tweetsByTrend[tweet.trend].append(tweet)
            else:
                tweetsByTrend[tweet.trend] = [tweet]
        
        return tweetsByTrend
    
    def createTrendLines(self, tweets):
        #break tweets list into groups of tweets of same trend
        #create trendline for each group
        #return trendlines
        tweetsByTrend = self.getTweetsByTrend(tweets)
        trendlines = Trendline()
        for trend in tweetsByTrend:
            trendline = self.createTrendLineFromTweets(tweetsByTrend[trend])
            trendlines.addTrendline(trendline)

        return trendlines
