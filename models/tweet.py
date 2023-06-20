from datetime import datetime
#this will contain our custom definition of tweet
#we need to have functions that will remove garbage from the tweet
class CustomTweet:
    def __init__(self) -> None:
        self.text = "" #whatever the content of tweet is
        self.trend = "" #we need to know what trend this tweet is related to

    def __init__(self, text, trend) -> None:
        self.text = text #whatever the content of tweet is
        self.trend = trend #we need to know what trend this tweet is related to
    
    def getTokenCount(self):
        return len(self.text.split(" "))
    
    def __str__(self):
        return f"CustomTweet(text='{self.text}', trend='{self.trend}')"
    


class Trendline:
    def __init__(self) -> None:
        #TrendlineItem
        self.trendlineItems = []
    
    def __init__(self, trendlineItems = []) -> None:
        #TrendlineItem
        self.trendlineItems = trendlineItems

    def addTrendline(self, trendline):
        self.trendlineItems.append(trendline)
    
    def getTrendlineByTrend(self, trend):
        for trendline in self.trendlineItems:
            if trendline.prompt == trend:
                return trendline
            
        return None


class TrendlineItem:
    def __init__(self) -> None:
        self.currentDateTime = datetime.now()
        self.tweets = []
        self.prompt = "" #prompt is unique to each trend

    def __init__(self,prompt, tweets = [],  currentDateTime = datetime.now()) -> None:
        self.currentDateTime = currentDateTime
        self.tweets = tweets
        self.prompt = prompt #prompt is unique to each trend
        

    def getCostOfPrompt(self):
        cost = 0.0
        for tweet in self.tweets:
            cost += tweet.getTokenCount() * (0.005/1000)


    def __str__(self):
        return f"TLine(text='{self.tweets}'')"
    