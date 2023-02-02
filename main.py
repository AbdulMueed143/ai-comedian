import tweepy
import concurrent.futures
import threading
import openai

# Set the API key
openai.api_key = "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"


# Your Twitter API credentials
consumer_key = 'xNMbL8Oqd4L0FkpJZa7afNzDB'
consumer_secret = 'RsFQo5GugF09yi70px9tpSKytjXoPveHM8WTi4oom2ZgQEmP1r'
access_token = '1052156414-mBsC0d3w5nNNma2tGlF3kyQnwTUmiHox5vqzsSM'
access_token_secret = '3dFbquLNNYtwGFfdHWunv1TdAMxyzGgMz75wYgfmjUUdH'


# Function to get the top 20 tweets for a trend
def get_tweets(trends, tweets):
    for trend in trends[0]["trends"]:
        tweets.extend(api.search_tweets(q=trend["name"], count=20))


def getTheJoke(trend, tweetsAsText):
    
    prompt = "I have following tweets "+tweetsAsText+" about the trend " +trend+ " Ricky Gervais"

    # Generate a response from GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response["choices"][0]["text"].strip()


if __name__ == "__main__":


    # Authenticate your API credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Initialize the API client
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print('Successful Authentication')
    except:
        print('Failed authentication')


    # Get the current trends for USA and Australia
    usa_trends = api.get_place_trends(2459115)  # WOEID for USA
    aus_trends = api.get_place_trends(1105779)  # WOEID for Australia

    # # Get the top 20 tweets for each trend
    # tweets = []
    # for trend in usa_trends[0]["trends"]:
    #     tweets.extend(api.search_tweets(q=trend["name"], count=20))
    # for trend in aus_trends[0]["trends"]:
    #     tweets.extend(api.search_tweets(q=trend["name"], count=20))

    # Create two threads to get the tweets for USA and Australia
    tweets = []
    thread1 = threading.Thread(target=get_tweets, args=(usa_trends, tweets))
    thread2 = threading.Thread(target=get_tweets, args=(aus_trends, tweets))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the threads to finish
    thread1.join()
    thread2.join()

    # Print the text of the tweets
    for tweet in tweets:
        print(tweet.text)

    thejoke = getTheJoke(tweet[0].text, )