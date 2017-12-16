import requests # This is for Python based HTTP
import json # This is for parsing the JSON response
import getnews

# This function uses the "requests" Python module
# to make a POST request to the Google NLP API web service 
# in order to analyze the sentiment of a news article, as in the
# Javascript exercise: https://codepen.io/mayacakmak/pen/dZoega

def getSentiment(text):
    # Construct the URL for a POST request
    baseUrl = "https://language.googleapis.com/v1/documents:analyzeSentiment";
    key = "key=AIzaSyBsj362-xU5nMLzBQiTSJ6aTg8uJ_zYR88"
    fullUrl = baseUrl + "?" + key 
    
    requestBody = { "document": 
                      { "type": "PLAIN_TEXT",
                        "language": "en",
                        "content": text
                      },
                     "encodingType": "NONE"}
    
    # Send the request and get the response
    r = requests.post(fullUrl, data=json.dumps(requestBody))
    
    isGoodNews = None
    # Check the status of the response to make sure it is OK
    if r.status_code == requests.codes.ok: # That is 200
        
        ## TODO: Parse the response into a dictionary.
        ## Check the response and set the isGoodNews variable accordingly.
        ## isGoodNews should be True if the news article has positive
        ## sentiment (i.e. positive score and non-zero magnitude). 
        
        pass ## You can remove this
    
    return isGoodNews

# The main script
if __name__ == "__main__":
        
    articles = getnews.getNewsArticles()
    
    ## TODO: Iterate over the news articles
    ## Check their sentiment using the getSentiment
    ## function defined above, which you will complete.
    ## Count the number of articles with positive sentiment and
    ## print a statement like "N out of M articles have
    ## good news today!"
    
