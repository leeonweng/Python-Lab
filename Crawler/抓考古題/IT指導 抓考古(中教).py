# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 01:24:25 2018

@author: Home love
"""

import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
#from urlparse import urljoin

url = 'http://210.240.188.241/ntculib_exam/?s1=100&s2=107&typeid=1&deptid=6&key=&button=%E6%9F%A5%E8%A9%A2'
html = requests.get(url)
html.encoding='utf-8'


sp=BeautifulSoup(html.text,"html.parser")

#建立目錄
pdf_dir="pdfs3/"
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
         full_path = "http://210.240.188.241/ntculib_exam" + href
    else:
         full_path = "http://http://210.240.188.241/ntculib_exam/_files/" + href
    print(full_path)
          
    try:
         filename = full_path.split('/')[-1]
         pdf = urlopen(full_path)
         f = open(os.path.join(pdf_dir,filename),'wb')
         f.write(pdf.read())
         f.close()
    except:
         print ("{} 無法讀取!".format(filename))
