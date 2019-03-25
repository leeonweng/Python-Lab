# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:50:04 2019

@author: Home love
"""

import requests,os
from bs4 import BeautifulSoup
#from PIL import Image
from urllib.request import urlopen

url='https://www.google.com/search?ei=7M1FXIq5N53g8wXfiYOACg&safe=off&yv=3&q=steak&tbm=isch&vet=10ahUKEwiK37CLgv_fAhUd8LwKHd_EAKAQuT0IPCgB.7M1FXIq5N53g8wXfiYOACg.i&ved=0ahUKEwiK37CLgv_fAhUd8LwKHd_EAKAQuT0IPCgB&ijn=1&start=100&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc'
re=requests.get(url)
sp=BeautifulSoup(re.text,'lxml')

img_dir='steak/'
if not os.path.exists(img_dir):
     os.mkdir(img_dir)
     print('資料夾建立完成')

print('下載中請稍後...')

img=sp.select('img')
for imgs in img:
     imgss=imgs.get('src')
     try:
          filename=imgss.split(':')[-1]+'.jpg'
          res=urlopen(imgss)
          f = open(os.path.join(img_dir,filename),'wb')
          f.write(res.read())
          f.close()
     except:
          print('{} 無法讀取!'.format(filename))


print('下載完畢!')