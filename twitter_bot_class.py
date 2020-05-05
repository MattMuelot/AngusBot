import tweepy
from my_auths import *
import random as r
import datetime


class TwitterBot:
    def __init__(self, quotes, this_day):
        self.auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        self.auth.set_access_token(CONSUMER_TOKEN, CONSUMER_SECRET)
        self.api = tweepy.API(self.auth)
        self.quotes = quotes
        self.this_day = this_day
        self.today_date = None
        self.my_hashes = ['#sports', '#dailyquotes', '#baseball', '#baseketball',
                          '#football', '#hockey']
        self.day_hashes = ['#sports', '#onthisday', '#baseball',
                           '#basketball', '#baseball', '#football', '#hockey', '#soccer']

    def post_quote(self):
        """Using Tweepy API, posts a random quote from the self.quotes attribute"""
        quote = r.choice(self.quotes) + '\n\n'
        for h in self.my_hashes:
            quote += f' {h}'
        self.api.update_status(quote)

    def set_date(self):
        """Sets the self.today_date attribute to the current date."""
        cur_date = datetime.datetime.today()
        cur_date = str(cur_date)
        self.today_date = cur_date[0:10]

    def new_date(self):
        """Using datetime, checks to see if the attribute self.today_date is still correct. If not,
        it runs the set_date() method."""
        date_check = datetime.datetime.today()
        date_check = str(date_check)
        if date_check[0:10] != self.today_date:
            self.set_date()
            return True
        else:
            return False

    def post_otd(self):
        """Using Tweepy API, posts a sporting event that took place on this date in the past from the
        self.this_day attribute."""
        otd = r.choice(self.this_day)
        new_otd = f'On This Day in {otd[0:4]}:\n{otd[5:]}\n\n'
        for h in self.day_hashes:
            new_otd += f' {h}'
        self.api.update_status(new_otd)
