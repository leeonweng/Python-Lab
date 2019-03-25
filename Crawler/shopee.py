# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:44:52 2018

@author: Home love
"""

import requests
from bs4 import BeautifulSoup

url = 'https://shopee.tw/api/v2/search_items/?by=relevancy&keyword=%E5%BA%8A%E5%8C%85&limit=50&match_id=37137599&newest=0&official_mall=1&order=desc&page_type=shop'

#res = requests.get(url)
#print (res.text)


headers = {'user-agent': 'Mozilla/5.0 (Macinton Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

res = requests.get(url,headers=headers)
print(res.request.headers)
print(res.text)