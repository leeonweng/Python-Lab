# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:38:01 2018

@author: Home love
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://learn.104.com.tw/cfdocs/edu/search/tool_class.cfm?no=12001006013")
soup = BeautifulSoup(html,"lxml")
print (soup.find_all("span",class_="style7"))