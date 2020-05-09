import tweepy
from my_auths import *


def create_api():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(CONSUMER_TOKEN, CONSUMER_SECRET)
    api = tweepy.API(auth)
    return api
