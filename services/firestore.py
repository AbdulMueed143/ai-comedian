import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from models.tweet import CustomTweet

class CustomFirebase:
    def __init__(self) -> None:
        # First, you'll need to initialize the SDK with your project's credentials
        self.cred = credentials.Certificate("services/comedian-ai-firebase.json")
        self.firebase = firebase_admin.initialize_app(self.cred)

        # Next, create a Firestore client
        self.db = firestore.client()

    

    # To save a CustomTweet object to Firestore:
    def saveTweet(self, tweet):
        # Create a dictionary to represent the object
        tweet_dict = {
            "text": tweet.text,
            "trend": tweet.trend,
        }
        # Add the dictionary to a Firestore collection
        self.db.collection("tweets").add(tweet_dict)

    # Using saveTweet, I want to save array of tweets to firestore
    def saveTweets(self, tweets):
        for tweet in tweets:
            self.saveTweet(tweet)

    # To read all CustomTweet objects from Firestore:
    def readTweets(self):
        # Get a reference to the "tweets" collection
        tweets_ref = self.db.collection("tweets")
        # Get all documents in the collection
        tweet_docs = tweets_ref.get()
        # Loop over the documents and create CustomTweet objects from them
        tweets = []
        for tweet_doc in tweet_docs:
            tweet_dict = tweet_doc.to_dict()
            tweet = CustomTweet()
            tweet.text = tweet_dict["text"]
            tweet.trend = tweet_dict["trend"]
            tweets.append(tweet)

        return tweets
