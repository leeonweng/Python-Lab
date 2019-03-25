# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:49:01 2019

@author: Home love
"""

import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://data.gov.tw/dataset/9621'
re=requests.get(url)
sp=BeautifulSoup(re.text,'lxml')
#print(sp)

csv_dir='大專校院各校科系別概況/'
if not os.path.exists(csv_dir):
     os.mkdir(csv_dir)
     print('資料夾建立中')
else:
     print('{} 資料夾建立完畢!'.format(csv_dir))

csv=sp.select('a')
#print(csv)
print('檔案下載中...')
for ss in csv:
     sss=ss.get('href')
#     print(sss)
     if(sss == None or sss.split('.')[-1] !='csv'):
          continue;
     try:
          filename=sss.split('/')[-1]
          res=urlopen(sss)
          f=open(os.path.join(csv_dir,filename),'wb')
          f.write(res.read())
          f.close()
     except:
          print('{} 檔案讀取失敗!'.format(filename))
print('下載完成!')