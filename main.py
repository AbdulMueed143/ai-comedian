from services.twitter import TwitterService
from services.utils import CleanTweets
from services.openai import Comedian


if __name__ == "__main__":
    twitterService = TwitterService()    
    twitterService.connectToTwitter()
    twitterService.getAllTrends()
    customTweets = twitterService.getTweets()

    # cleanTweets  = CleanTweets()

    # cleanTweets.readTweetsFromFile("allTweets.txt")
    # tweetsCleaned  = cleanTweets.removeTagsFromTweets()

    # rickyJervais = Comedian("Ricky Gervais")
    # kevinHart = Comedian("Kevin Hart")
    # ckLouis = Comedian("CK Louis")

    # rickyJervais.createPromptForJoke(tweetsCleaned)

    # rickyJervais.writeJoke()


    


    print(tweetsCleaned)

