# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 10:05:49 2018

@author: Home love
"""

import requests
from bs4 import BeautifulSoup

rs = requests.get(
          url = 'https://www.ptt.cc/bbs/Gossiping/index.html',
          cookies = {'over18':'1'})

bs = BeautifulSoup(rs.text,'html.parser')

pagination = bs.find('div', {'class':'btn-group-paging'}).find_all('a', {'class':'btn'})
next_page = pagination[1]['href']
total_page = next_page.replace('/bbs/Gossiping/index', '')
total_page = int(total_page[:-5]) + 1
links = list()
#for i in range(總頁數, 總頁數 - 想爬的頁數, -1):
for i in range(100, 100 - 20, -1):
     link = 'https://www.ptt.cc/bbs/Gossiping/index' + str(i) + '.html'
     print (links.append(link))
