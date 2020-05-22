import tweepy
import time
from my_auths import *


def create_api():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(CONSUMER_TOKEN, CONSUMER_SECRET)
    api = tweepy.API(auth)
    return api


# noinspection PyBroadException
class Listener(tweepy.StreamListener):
    def __init__(self, api):
        super().__init__()
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                tweet.favorite()
                print('Liked')
                time.sleep(30)
            except Exception as e:
                time.sleep(30)
                pass


def main(keywords):
    api = create_api()
    tweets_listener = Listener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=['en'])


while True:
    try:
        main(['sports', 'baseball', 'basketball', 'football', 'soccer', 'nba', 'mlb', 'nfl'])
        time.sleep(60)
    except:
        time.sleep(120)
