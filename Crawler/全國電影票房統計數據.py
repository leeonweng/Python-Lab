# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:09:46 2018

@author: Home love
"""

import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
#from urlparse import urljoin

url = 'https://data.gov.tw/dataset/94224'
html = requests.get(url)
html.encoding='utf-8'


sp=BeautifulSoup(html.text,"html.parser")

#建立目錄
csv_dir="csvs/"
if not os.path.exists(csv_dir):
     os.mkdir(csv_dir)


links=sp.find_all("a")
for link in links:
    href=link.get("href")
    attrs=[href]          
    for attr in attrs:
        if href != None and href.startswith("http://"):
          full_path = attr
          filename = full_path.split('/')[-1]
          print(full_path)
          try:
              csv = urlopen(full_path)
              f = open(os.path.join(csv_dir,filename),'wb')
              f.write(csv.read())
              f.close()
          except:
               print ("{} 無法讀取!".format(filename))