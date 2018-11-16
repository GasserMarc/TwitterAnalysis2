import tweepy
from credentials import *

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


def collect(Search):
    connexion = twitter_setup()
    tweets = connexion.search(q=str(Search),language="french",rpp=100,show_user=True)
    for tweet in tweets:
        print(tweet.text)
