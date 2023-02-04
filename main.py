from services.twitter import TwitterService
import tweepy


if __name__ == "__main__":
    # # Get the top 20 tweets for each trend
    # tweets = []
    # for trend in usa_trends[0]["trends"]:
    #     tweets.extend(api.search_tweets(q=trend["name"], count=20))
    # for trend in aus_trends[0]["trends"]:
    #     tweets.extend(api.search_tweets(q=trend["name"], count=20))

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