# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:11:59 2019

@author: Home love
"""

from bs4 import BeautifulSoup
import requests
re = requests.get("https://news.google.com/rss/search?q=NBA&hl=zh-TW&gl=TW&ceid=TW:zh-Hant")  
soup = BeautifulSoup(re.text,'html.parser')
print(soup)

rs=soup.find_all('title')
print(rs)
# 二、找到element
## 透過tag名稱尋找元素(第一個，回傳一個元素類別)
#elem = soup.find('a')
#print(elem)
#print("----------------------------------")
## 透過tag名稱尋找元素(全部，回傳一個元素類別「陣列」)
#elems = soup.find_all('a')
#for elem in elems:
#    print(elem)
#print("----------------------------------")

#selector = "#quick-start > h1"
#elem = soup.select(selector)
#print(elem)
#print("----------------------------------")