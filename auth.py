from twitter import Twitter, OAuth, TwitterHTTPError

def getTwitter():
    OAUTH_TOKEN = ''
    OAUTH_SECRET = ''
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''

    return Twitter(
        auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))