# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 10:32:13 2019

@author: Home love
"""

import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://www.google.com/search?biw=1920&bih=948&tbm=isch&sa=1&ei=93RKXKPWO8aX8gXhv7P4BA&q=%E6%B2%B9%E9%9B%9E%E8%85%BF&oq=%E7%94%B1%E9%9B%9E%E8%85%BF&gs_l=img.3.0.0i10i24.4800.5040..6543...0.0..0.112.259.2j1......0....1..gws-wiz-img.6XUlhVqe2Eg'
re=requests.get(url)
sp=BeautifulSoup(re.text,'lxml')
#print(sp)

img_dir='chicken/'
if not os.path.exists(img_dir):
     os.mkdir(img_dir)
     print('資料夾建立中...')
else:
     print('{}資料夾建立完成!'.format(img_dir))
     
img=sp.select('img')
#print(img)
print('資料下載中,請稍後...')
for imgs in img:
     imgss=imgs.get('src')
     #print(imgss)
     try:
          filename=imgss.split(':')[-1]+'.jpg'
          res=urlopen(imgss)
          f=open(os.path.join(img_dir,filename),'wb')
          f.write(res.read())
          f.close()
     except:
          print('{} 無法讀取!'.format(filename))
print('下載完畢!')