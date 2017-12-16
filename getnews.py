import requests # This is for Python based HTTP
import json # This is for parsing the JSON response
import pyttsx3 # This is for text-to-speech
from os import system

# This function uses the "requests" Python module
# to make a GET request to the newsapi.org web 
# service. It replicates the functionality of an earlier
# Javascript exercise: https://codepen.io/mayacakmak/pen/zPOKyg
 
def getNewsArticles():
    # Define variable to be returned
    articles = None
    
    # Construct the URL for a GET request
    baseUrl = "https://newsapi.org/v1/articles"
    param1 = "source=the-next-web"
    param2 = "sortBy=latest"
    param3 = "apiKey=259037180dcc4308a7ce6d418d83ff3b"
    fullUrl = baseUrl + "?" + param1 + "&" + param2 + "&" + param3 
    
    # Send the request and get the response
    r = requests.get(fullUrl)
    
    # Check the status of the response to make sure it is OK
    if r.status_code == requests.codes.ok: # That is 200
        # Parse the JSON response into a dictionary
        response = json.loads(r.text)
        articles = response['articles']
        print("Received", len(articles), "articles.")
        
    return articles


def getShortestArticleIndex(articles):

    # TODO: Iterate over the received articles
    # For each article count the number of words in the
    # article description. Return the index of the one
    # with fewest words.
    return 0


# This function uses text-to-speech to say the text in
# the "description" parameter
def readText(description):
    engine = pyttsx3.init()
    engine.say(description)
    engine.runAndWait()

# Another way to do text to speech
def readTextAlt(description):
    description = description.replace("'", "")
    system("say " + description)


# The main script
if __name__ == "__main__":
        
    articles = getNewsArticles()
    shortestIndex = getShortestArticleIndex(articles)
    shortestArticle = articles[shortestIndex]
    readTextAlt(shortestArticle['description'])
    print("Shortest article today:\n", shortestArticle['description'])
