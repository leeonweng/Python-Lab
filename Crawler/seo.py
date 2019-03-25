# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 10:19:09 2019

@author: User
"""

import requests,os
from bs4 import BeautifulSoup

url='https://www.awoo.com.tw/blog/2018/02/technical-or-content/'
res = requests.get(url)
sp = BeautifulSoup(res.text,'lxml')

data = sp.find_all('a')

for text in data:
    f = sp.text
#    print (f)
    
    with open ('seo是什麼.txt','w',encoding='utf-8') as w:
        w.write(f)
        
#print (data)