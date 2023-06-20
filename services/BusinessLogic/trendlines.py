from models.tweet import Trendline, TrendlineItem
from services.utils import CleanTweets
from services.openai import Comedian

class TrendLineManipulation:
    def __init__(self) -> None:
        pass

    #This method expects tweets of specific trend only
    def createTrendLineItemFromTweets(self, tweets):
        ckLouis = Comedian("CK Louis")
        prompt = ckLouis.createPromptForJoke(tweets)
        return TrendlineItem(prompt, tweets)
    
    def getTweetsByTrend(self, tweets):
        tweetsByTrend = {}
        for tweet in tweets:
            if tweet.trend in tweetsByTrend:
                tweetsByTrend[tweet.trend].append(tweet)
            else:
                tweetsByTrend[tweet.trend] = [tweet]
        
        return tweetsByTrend
    
    def createTrendLine(self, tweets):
        #break tweets list into groups of tweets of same trend
        #create trendline for each group
        #return trendlines
        tweetsByTrend = self.getTweetsByTrend(tweets)
        trendline = Trendline()
        for trend in tweetsByTrend.keys():
            item = self.createTrendLineItemFromTweets(tweetsByTrend[trend])
            trendline.trendlineItems.append(item)

        return trendline
