# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class WebScrape:
    def __init__(self):
        self.quotes = []
        self.this_day = []

    def grab_quotes(self):
        """Scrapes the websites, held in variable lk. Grabs all the quotes and puts them into the
        attribute self.quotes."""
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

    def grab_on_this_day(self):
        """Scrapes the website, held in variable lk. Grabs all events and adds them to
        attribute self.this_day."""
        lk = 'https://www.onthisday.com/sport/events.php'
        page_load = requests.get(lk)
        soup = BeautifulSoup(page_load.content, 'html.parser')
        for l in soup.find_all('li', class_='event'):
            if l.text not in self.this_day:
                self.this_day.append(l.text)

    def return_quotes(self):
        """Returns attribute."""
        return self.quotes

    def return_otd(self):
        """Returns attribute."""
        return self.this_day
