# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:28:06 2019

@author: Home love
"""

import requests,os
from bs4 import BeautifulSoup
url='https://comicbus.com/html/103.html'
headers = {
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
          }

re = requests.get(url,headers=headers)
re.encoding= 'big5'
sp = BeautifulSoup(re.text,'html5lib')
al = sp.find_all('a')
print(al)