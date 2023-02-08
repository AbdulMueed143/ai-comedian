import re


class CleanTweets:
    tweets = []
    cleanedTweets = []

    def readTweetsFromFile(self,filename):
        with open("allTweets.txt", "r", encoding="utf8") as file:
            # Read the contents of the file as a single string
            content = file.read()
            self.tweets = content.split(",")

        return self.tweets
    
    def removeTagsFromTweets(self):
        patterns = ["https?://.*?([,\"\' ])|RT\s@\w+|\@\w+|\\n|\\\\n"]

        for tweet in self.tweets:
            # Apply the regular expression to the value
            for pattern in patterns:
                self.cleanedTweets.append(re.sub(pattern, "", tweet))
        
        return self.cleanedTweets

    def readTweetsFromDatabase(self):
        pass