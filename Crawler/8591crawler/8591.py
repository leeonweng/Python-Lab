# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 20:51:46 2019

@author: Home love
"""

import requests as rq
from bs4 import BeautifulSoup as bs

url = 'https://www.8591.com.tw/mallList-list.html?searchGame=859'
r = rq.get(url)
soup = bs(r.text,'lxml')
#print(soup)

a = soup.find_all('a')
print(a)


for al in a:
     als = al.get('href')
     buys = al.get('buyStatus')
     titles = al.get('title')
     print(titles)
     

'''
def autoparts():
     parts_dict={}   
     list_of_parts = open('list_of_parts.txt', 'r')   
     for line in list_of_parts:
          k, v = line.split()
          parts_dict[k] = v   
          return parts_dict

'''  