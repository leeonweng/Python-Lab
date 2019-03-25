# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:00:18 2018

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
    if (href == None or href.split('.')[-1]!='pdf'):
         continue;
    if(href[0:4]=='http'):
         full_path = href
    elif(href[0]=='/'):
         full_path = "http://academic.ntue.edu.tw" + href
    else:
         full_path = "http://academic.ntue.edu.tw/ezfiles/" + href
    print(full_path)
          
    try:
         filename = full_path.split('/')[-1]
         pdf = urlopen(full_path)
         f = open(os.path.join(pdf_dir,filename),'wb')
         f.write(pdf.read())
         f.close()
    except:
         print ("{} 無法讀取!".format(filename))
