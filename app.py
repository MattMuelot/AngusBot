# -*- coding: utf-8 -*-

from scrape_app import *
from twitter_bot_class import *
import time as t

scrape = WebScrape()
scrape.grab_quotes()
scrape.on_this_day()
my_bot = TwitterBot(scrape.quotes, scrape.this_day)

while True:
    try:
        current_date = my_bot.new_date()
        if current_date:
            my_bot.post_otd()
            t.sleep(9000)
        else:
            my_bot.post_quote()
            t.sleep(25000)
    except:
        pass
