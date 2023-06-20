import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from models.tweet import CustomTweet
from models.tweet import Trendline, TrendlineItem
from datetime import datetime

class CustomFirebase:
    def __init__(self) -> None:
        # First, you'll need to initialize the SDK with your project's credentials
        self.cred = credentials.Certificate("services/comedian-ai-firebase.json")
        self.firebase = firebase_admin.initialize_app(self.cred)

        # Next, create a Firestore client
        self.db = firestore.client()
        self.trendlines_ref = self.db.collection('trendlines')
        self.project_id = "comedian-ai"
    
    #expecting trendline object
    def saveTrendlines(self, trendline):
        trendline_dict = self._trendlineToDict(trendline)
        #convert trendline_dict['currentDateTime'] into string of date and only hour but from 24 hour formate
        doc_reference = trendline_dict['currentDateTime'].strftime('%Y-%m-%d %H:00:00')
        trendline_doc_ref = self.trendlines_ref.document(doc_reference)
        trendline_dict['projectId'] = self.project_id
        trendline_doc_ref.set(trendline_dict)
    
    # def getTrendlineByPrompt(self, prompt):
    #     trendline_doc_ref = self.trendlines_ref.document(prompt)
    #     trendline_dict = trendline_doc_ref.get().to_dict()
    #     if trendline_dict is None:
    #         return None
    #     return self._dictToTrendline(trendline_dict)

    def getAllTrendlines(self):
        trendlines = []
        docs = self.trendlines_ref.stream()
        for doc in docs:
            trendline_dict = doc.to_dict()
            trendline = self._dictToTrendline(trendline_dict)
            trendlines.append(trendline)
        return trendlines
    
    def _trendlineToDict(self, trendline):
        trendline_dict = {}
        trendline_dict['trendlineItems'] = []
        trendline_dict['currentDateTime'] = datetime.now()

        #this has items and each item consists of tweets
        for trendline_item in trendline.trendlineItems:
            trendline_item_dict = {}
            trendline_item_dict['prompt'] = trendline_item.prompt
            trendline_item_dict['tweets'] = []
            for tweet in trendline_item.tweets:
                tweet_dict = {}
                tweet_dict['text'] = tweet.text
                tweet_dict['trend'] = tweet.trend
                tweet_dict['tokenCount'] = tweet.getTokenCount()
                trendline_item_dict['tweets'].append(tweet_dict)

            trendline_dict['trendlineItems'].append(trendline_item_dict)

        return trendline_dict
    
    def _dictToTrendline(self, trendline_dict):
        trendline = Trendline()
        # trendline.currentDateTime = datetime.strptime(trendline_dict['currentDateTime'], '%Y-%m-%d %H:%M:%S')
        for trendline_item_dict in trendline_dict['trendlineItems']:
            trendline_item = TrendlineItem([], trendline_item_dict['prompt'], datetime.strptime(trendline_item_dict['currentDateTime'], '%Y-%m-%d %H:%M:%S'))
            for tweet_dict in trendline_item_dict['tweets']:
                tweet = CustomTweet(tweet_dict['text'], tweet_dict['trend'])
                trendline_item.tweets.append(tweet)
            trendline.trendlineItems.append(trendline_item)

        return trendline