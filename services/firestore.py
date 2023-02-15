import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# First, you'll need to initialize the SDK with your project's credentials
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Next, create a Firestore client
db = firestore.client()

# To save a CustomTweet object to Firestore:
def save_tweet(tweet):
    # Create a dictionary to represent the object
    tweet_dict = {
        "text": tweet.text,
        "wordCount": tweet.wordCount,
        "trend": tweet.trend,
    }
    # Add the dictionary to a Firestore collection
    db.collection("tweets").add(tweet_dict)

# To read all CustomTweet objects from Firestore:
def read_tweets():
    # Get a reference to the "tweets" collection
    tweets_ref = db.collection("tweets")
    # Get all documents in the collection
    tweet_docs = tweets_ref.get()
    # Loop over the documents and create CustomTweet objects from them
    tweets = []
    for tweet_doc in tweet_docs:
        tweet_dict = tweet_doc.to_dict()
        tweet = CustomTweet()
        tweet.text = tweet_dict["text"]
        tweet.wordCount = tweet_dict["wordCount"]
        tweet.trend = tweet_dict["trend"]
        tweets.append(tweet)
    return tweets
