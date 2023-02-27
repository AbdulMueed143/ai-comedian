from services.twitter import TwitterService
from services.utils import CleanTweets
from services.openai import Comedian
from services.BusinessLogic.trendlines import TrendLineManipulation


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
    trendlines = TrendLineManipulation().createTrendLines(cleanTweets.tweets).trendlineItems

    # print all prompts from trendlines
    for trendline in trendlines:
        for trendlineItem in trendline.trendlineItems:
            print(trendlineItem.prompt)


    #we should save trendlines to server :) 

    # rickyJervais = Comedian("Ricky Gervais")
    # kevinHart = Comedian("Kevin Hart")
    # ckLouis = Comedian("CK Louis")

    # rickyJervais.createPromptForJoke(tweetsCleaned)

    # rickyJervais.writeJoke()


    # print(tweetsCleaned)

    # print(customTweets)

