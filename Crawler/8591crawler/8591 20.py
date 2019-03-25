# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:32:10 2019

@author: Home love
"""

import requests as re
from bs4 import BeautifulSoup as bs

class GetData:
     header = {
               'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
               }
     hrefs_list=list()
     titles_list=list()
     buyStatus_list=list()
     
     def __init__(self, input_url):
        self.url = input_url
        html = re.get(self.url)
        self.soup = bs(html.text, 'lxml')
     
     def get_index(self):
        atags = self.soup.find_all('a',{'class':'ml-item-title'})
        for atag in atags:
            pat = re.findall(r'\.', atag.get('title'))
            if pat: return pat