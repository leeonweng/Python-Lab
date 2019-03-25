# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 22:22:07 2018

@author: Home love
"""

import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
#headers ={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
url = ('https://tw.observer/search/%23%E8%A5%BF%E6%96%AF')
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
imgs = soup.select('img')
#print(imgs)

#建立目錄
img_dir="imgs2/"
if not os.path.exists(img_dir):
     os.mkdir(img_dir)

for img in imgs:
    try:
        fn = img['src']
        print(fn)
        img=urlopen(fn)
    except Exception as e:
        print (e)
    continue
    with open('./imgs/' + str(fn), 'wb') as f:
            f.write(img.read())

"""            
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
"""