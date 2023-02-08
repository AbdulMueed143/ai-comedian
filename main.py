from services.twitter import TwitterService
from services.utils import CleanTweets

if __name__ == "__main__":
    # twitterService = TwitterService()    
    # twitterService.connectToTwitter()
    # trends = twitterService.getAllTrends()
    # tweets = twitterService.getTweets()

    # f = open("allTweets.txt", "a")
    # f.write(str(tweets))
    # f.close()

    cleanTweets  = CleanTweets()

    tweets = cleanTweets.readTweetsFromFile("allTweets.txt")
    tweetsCleaned  = cleanTweets.removeTagsFromTweets()

    print(tweetsCleaned)

