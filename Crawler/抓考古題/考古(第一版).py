# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 22:23:12 2018

@author: Home love
"""

import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
#from urlparse import urljoin

url = 'http://academic.ntue.edu.tw/files/11-1007-467.php'
html = requests.get(url)
html.encoding='utf-8'


sp=BeautifulSoup(html.text,"html.parser")

#建立目錄
pdf_dir="pdfs/"
if not os.path.exists(pdf_dir):
     os.mkdir(pdf_dir)


links=sp.find_all("a")
for link in links:
    href=link.get("href")
    attrs=[href]          
    for attr in attrs:
        if href != None and href.startswith("http://academic.ntue.edu.tw"):
          full_path = attr
          filename = full_path.split('/')[-1]
          print(full_path)
          try:
              pdf = urlopen(full_path)
              f = open(os.path.join(pdf_dir,filename),'wb')
              f.write(pdf.read())
              f.close()
          except:
               print ("{} 無法讀取!".format(filename))
