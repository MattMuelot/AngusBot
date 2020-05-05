# -*- coding: utf-8 -*-

import tweepy
from my_auths import *
import time as t
import random as r
import requests
from bs4 import BeautifulSoup
import datetime


class MyApp:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        self.auth.set_access_token(CONSUMER_TOKEN, CONSUMER_SECRET)
        self.api = tweepy.API(self.auth)
        self.quotes = []
        self.this_day = []
        self.my_date = None
        self.my_hashes = ['#sports', '#dailyquotes', '#baseball', '#baseketball',
                          '#football', '#hockey']
        self.day_hashes = ['#sports', '#onthisday', '#baseball',
                           '#basketball', '#baseball', '#football', '#hockey', '#soccer']

    def grab_quotes(self):
        lk = 'https://www.keepinspiring.me/100-most-inspirational-sports-quotes-of-all-time/'
        page_load = requests.get(lk)
        soup = BeautifulSoup(page_load.content, 'html.parser')
        for d in soup.find_all('div', class_='author-quotes'):
            if 'ezslot' in d.text:
                pass
            else:
                if d.text not in self.quotes:
                    self.quotes.append(d.text)
                else:
                    pass
        lk = 'https://everydaypower.com/motivational-sports-quotes/'
        page_load = requests.get(lk)
        soup = BeautifulSoup(page_load.content, 'html.parser')
        all_p = []
        for p in soup.find_all('p'):
            if p.text not in all_p:
                all_p.append(p.text)
        new_p = []
        for i in all_p:
            new_str = i.replace('”', '"')
            new_str = new_str.replace('“', '"')
            new_p.append(new_str)
        for i in new_p:
            final_str = ''
            if '"' in i:
                i_split = i.split('"')
                final_str = '"' + i_split[1] + '"'
                final_str += i_split[2]
                if final_str not in self.quotes:
                    self.quotes.append(final_str)

    def send_inspiration(self):
        quote = r.choice(self.quotes)
        self.quotes.remove(quote)
        quote = r.choice(self.quotes) + '\n\n'
        for h in self.my_hashes:
            quote += f' {h}'
        self.api.update_status(quote)
        print(quote)
        print()

    def send_on_this_day(self):
        otd = r.choice(self.this_day)
        new_otd = f'On This Day in {otd[0:4]}:\n{otd[5:]}\n\n'
        for h in self.day_hashes:
            new_otd += f' {h}'
        self.api.update_status(new_otd)
        print(new_otd)
        print()

    def on_this_day(self):
        lk = 'https://www.onthisday.com/sport/events.php'
        page_load = requests.get(lk)
        soup = BeautifulSoup(page_load.content, 'html.parser')
        for l in soup.find_all('li', class_='event'):
            if l.text not in self.this_day:
                self.this_day.append(l.text)

    def set_date(self):
        cur_date = datetime.datetime.today()
        cur_date = str(cur_date)
        self.my_date = cur_date[0:10]

    def check_date(self):
        date_check = datetime.datetime.today()
        date_check = str(date_check)
        if date_check[0:10] != self.my_date:
            return True
        else:
            return False


m = MyApp()
m.grab_quotes()
m.set_date()
m.on_this_day()
m.send_on_this_day()

print('Initializing')
print()

while True:
    try:
        d_check = m.check_date()
        if d_check is True:
            m.send_on_this_day()
        else:
            pass
        m.send_inspiration()
        t.sleep(43200)
    except tweepy.TweepError:
        print('Duplicate')
        continue
