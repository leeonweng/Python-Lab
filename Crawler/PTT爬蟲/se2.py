# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 02:17:14 2019

@author: User
"""

import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
#from urlparse import urljoin

url = 'https://www.ptt.cc/bbs/sex/M.1549298010.A.B54.html'
res = requests.get(url=url,cookies={'over18':'1'})
res.encoding='utf-8'
ct = BeautifulSoup(res.text,'lxml')

#print(ct)

#建立目錄
img_dir="sex2_imgs/"
if not os.path.exists(img_dir):
     os.mkdir(img_dir)
     print('資料夾建立中...')
else:
    print('資料夾建立完畢!')
    
print('檔案下載中,請稍後!')

links=ct.find_all("a")
for link in links:
    href=link.get("href")
#    print(href)
    if (href == None or href.split('.')[-1]!='jpg'):
        continue;
    if(href[0:4]=='http'):
        full_path = href
    elif(href[0]=='/'):
        full_paht = 'https:' + href
    else:
        full_path = 'https://imgur.com/' + href
    print(full_path)
    
    try:
        filename = full_path.split('/')[-1]
        img = urlopen(full_path)
        f = open(os.path.join(img_dir,filename),'wb')
        f.write(img.read())
        f.close()
    except:
        print ("{} 無法讀取!".format(filename))
        
print('下載完畢!')
