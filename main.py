from services.twitter import TwitterService
from services.utils import CleanTweets
from services.openai import Comedian
from services.BusinessLogic.trendlines import TrendLineManipulation
from services.firestore import CustomFirebase


if __name__ == "__main__":
    # twitterService = TwitterService()    
    # twitterService.connectToTwitter()
    # twitterService.getAllTrends()
    # customTweets = twitterService.getTweets()

    cleanTweets  = CleanTweets()
    # cleanTweets.tweets = customTweets
    # cleanTweets.writeTweetsToFile(customTweets)
    
    cleanTweets.readTweetsFromJsonFile()
    tweetsCleaned  = cleanTweets.removeTagsFromTweets()
    #1 trend line is for all the prompts of different time 
    #2 when the script runs again another trend line is created
    trendline = TrendLineManipulation().createTrendLine(cleanTweets.tweets)

    #we should save trendlines to server :) 
    #lets save it to server
    firebase = CustomFirebase()
    #loop trendlines key value pair
    #for each trendline, save it to firestore
    # firebase.saveTrendlines(trendline)
    trendlines = firebase.getAllTrendlines()

    # rickyJervais = Comedian("Ricky Gervais")
    # kevinHart = Comedian("Kevin Hart")
    # ckLouis = Comedian("CK Louis")

    # rickyJervais.createPromptForJoke(tweetsCleaned)

    # rickyJervais.writeJoke()


    # print(tweetsCleaned)
    # print(customTweets)

