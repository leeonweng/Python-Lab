# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 09:58:29 2018

@author: liwei
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://www.104.com.tw/jobs/search/?keyword=%E5%B7%A5%E7%A8%8B%E5%B8%AB&jobsource=joblist_a_relevance&ro=0&order=1")
soup = BeautifulSoup(html,"lxml")
print(soup.get_text("|", strip=True))
