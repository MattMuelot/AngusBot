# -*- coding: utf-8 -*-

from twitter_bot_class import *
from bot_api import create_api

my_bot = TwitterBot(create_api())
my_bot.bot_mainloop()
