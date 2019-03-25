# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:49:57 2018

@author: Home love
"""
import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://olis.ncue.edu.tw/sp.asp?xdurl=mp1ap/ExFileList.asp&classtype=1&coll_xitem=6&dept_xitem=5&mp=1'
html = requests.get(url)
html.encoding='utf-8'


sp=BeautifulSoup(html.text,"html.parser")

#建立目錄
pdf_dir="pdfs2/"
if not os.path.exists(pdf_dir):
     os.mkdir(pdf_dir)

links=sp.find_all("a")
for link in links:
     href=link.get("href")
	
	#如果不是 .pdf 結尾，直接跳過不處理
     if(href == None or href.split('.')[-1]!='pdf'):
          continue;	
	#關於網址的處理
     if(href[0:5]=='https'):
          full_path = href
     elif(href[0]=='/'): #這邊要處理開頭為 / 的網址
          full_path = "https://olis.ncue.edu.tw" + href
     else: #其他的是相對路徑
		    full_path= "https://olis.ncue.edu.tw/" + href
     print(full_path)
     
     try:
          filename = full_path.split('/')[-1]
          pdf = urlopen(full_path)
          f = open(os.path.join(pdf_dir,filename),'wb')
          f.write(pdf.read())
          f.close()
     except:
          print ("{} 無法讀取!".format(filename))
	
	#後面就是抓 full_path 並儲存