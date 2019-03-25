# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:55:35 2019

@author: Home love
"""

#import requests 
from bs4 import BeautifulSoup
import urllib.request as req

url='https://www.ptt.cc/bbs/movie/index.html'
#建立一個Request物件,附加Request Headers的資訊
request=req.Request(url,headers={
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'})

with req.urlopen(request) as response:
     data=response.read().decode('utf-8')
#print(data)

root=BeautifulSoup(data,'html.parser')
titles=root.find_all('div',class_='title') #尋找所有class='title'的div標籤
for title in titles:
     if title.a != None:#如果標題包含a標籤(沒有被刪除) 印出來
          print(title.a.string)
     