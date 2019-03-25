# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:16:49 2018

@author: Home love
"""

import requests
from bs4 import BeautifulSoup
url="https://www.ptt.cc/bbs/NBA/index.html"

def get_NBA(url):
     r = requests.get(url)
     sp = BeautifulSoup(r.text,"html.parser")
     rs = sp.select('.r-ent')
     for item in rs:
          print ('日期:',item.select('.date')[0].text)
          print ('推文數:',item.select('.nrec')[0].text)
          print ('作者:',item.select('.author')[0].text)
          print ('標題:',item.select('.title')[0].text)
          print ('==============================================')
          f = open("D:/Desktop/Coding/python/PTT爬蟲/NBA try.txt",'a')
          f.write(item)


for page in range(0,4):
    r = requests.get(url)
    sp = BeautifulSoup(r.text,"html.parser")
    btn = sp.select('div.btn-group > a')
    up_page_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_href
    url = next_page_url
    get_NBA(url = url)