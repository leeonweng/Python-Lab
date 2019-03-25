# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:12:41 2019

@author: User
"""
import requests as req
import os
from bs4 import BeautifulSoup as bfs
from urllib.request import urlopen

url = 'http://m.ting-wen.com/oldexam/list/58?p=35'
re = req.get(url)
re.encoding = 'uft-8'
sp = bfs(re.text,'html.parser')
#print(sp)
df = sp.select('a')

pdf_dir="pdfs國考/"
if not os.path.exists(pdf_dir):
     os.mkdir(pdf_dir)

for src in df:
    href = src.get('href')
    if (href == None or href.split('.')[-1] != ('pdf')):
        continue;
    elif (href[0:4]=='http'):
        full_href = href
    else:
        not print
    print(full_href)
    
    try:
        filename = full_href.split('/')[-1]
        pdf = urlopen(full_href)
        f = open(os.path.join(pdf_dir,filename),'wb')
        f.write(pdf.read())
        f.close()
    except:
        print ("{} 無法讀取!".format(filename))
