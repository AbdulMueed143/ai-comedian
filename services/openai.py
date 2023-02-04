'''
Working with open ai to get the jokes
'''
import openai

class OpenAIService:
    # Set the API key
    openai.api_key = ""

    def connect(self):
        pass

    def sendRequestToGpt3(self, prompt):
        #Generate a response from GPT-3
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        return response["choices"][0]["text"].strip()
    
    #prompt = "I have following tweets "+tweetsAsText+" about the trend " +trend+ " Ricky Gervais"


#Prompt Generation should itself be a class with different processes to generate different prompts
class CreateJokes:
    def __init__(self) -> None:
        pass

    def createPromptForJokeWithComedian(self, comedian, trend, tweets):
        pass


#Currently we only have names of comedians in list
#But in future we might need way more than this
#We will not use this class for now
class Comedian:
    name = ""