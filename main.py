from services.twitter import TwitterService

if __name__ == "__main__":
    # twitterService = TwitterService()    
    # twitterService.connectToTwitter()
    # trends = twitterService.getAllTrends()
    # tweets = twitterService.getTweets()

    # f = open("allTweets.txt", "a")
    # f.write(str(tweets))
    # f.close()

    f = open("allTweets.txt", "r")
    tweets = f.read()
    f.close()

    print(tweets)