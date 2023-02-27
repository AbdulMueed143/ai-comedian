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
    


class Trendline:
    def __init__(self) -> None:
        #TrendlineItem
        self.trendlineItems = []

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


    def __init__(self, tweets, prompt, currentDateTime = datetime.now()) -> None:
        self.currentDateTime = currentDateTime
        self.tweets = tweets
        self.prompt = prompt #prompt is unique to each trend
    