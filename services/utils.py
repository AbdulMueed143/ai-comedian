import re
import json
from models.tweet import CustomTweet


class CleanTweets:
    tweets = []
    cleanedTweets = []

    #Write custon tweets object to json file
    def writeTweetsToFile(self, tweets):
        json_data = json.dumps([tweet.__dict__ for tweet in tweets], indent=4)
        # Write the JSON data to a file
        with open('tweets.json', 'w') as f:
            f.write(json_data)

    def readTweetsFromJsonFile(self):
        self.tweets.clear()

        # Read the JSON data from the file
        with open('tweets.json', 'r') as f:
            json_data = f.read()
            # Parse the JSON data into a list of dictionaries
            tweets_data = json.loads(json_data)

        for tweet_data in tweets_data:
            tweet = CustomTweet(tweet_data['text'], tweet_data['trend'])
            self.tweets.append(tweet)

        return self.tweets

    def removeTagsFromTweets(self):
        self.cleanedTweets.clear()
        
        patterns = ["https?://.*?([,\"\' ])|RT\s@\w+|\@\w+|\\n|\\\\n"]

        for tweet in self.tweets:
            # Apply the regular expression to the value
            for pattern in patterns:
                self.cleanedTweets.append(re.sub(pattern, "", tweet.text))
        
        return self.cleanedTweets

    def readTweetsFromDatabase(self):
        pass