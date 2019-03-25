# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:14:37 2018

@author: Home love
"""

# ptt extraction
import requests
from bs4 import BeautifulSoup

rs = requests.get(
          url = 'https://www.ptt.cc/bbs/Gossiping/index.html',
          cookies = {'over18':'1'})

bs = BeautifulSoup(rs.text,'html.parser')
rows = bs.find_all('div',{'class':'r-ent'})
#rows = bs.find_all('a')

posts = list()
for row in rows:
     meta = row.find('div','title').find('a')
     if meta:
          posts.append({
               'link':meta['href'],
               'title':meta.text,
               'date':meta.find('div','date')[0].text,
               'author':meta.find('div','author')[0].text,
               'push':meta.find('div','nrec')[0].text
          })    
     print(row)