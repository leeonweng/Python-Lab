# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:17:50 2019

@author: Home love
"""

import requests as rq ,json
from bs4 import BeautifulSoup

#利用get取得API資料
url = ('https://www.dcard.tw/f/dressup')
res = rq.get(url)
sp = BeautifulSoup(res.text,'html.parser')
print(sp)
with open('dca爬爬.txt',mode='w',encoding='utf-8')as file:
     file.write(str(sp))
#利用json.loads()解碼json
resjson = json.loads(res.text)
print(resjson)


#透過API了解發文者性別
gender = {'F':0,'M':0}
for content in resjson:
     gender[content['gender']]+=1
     
import matplotlib.pyplot as plt
#data = [35,15,85,35,20]
#plt.bar(range(len(data)),data)
#plt.show()
kind = ['boy','girl']
data = [gender['F'],gender['M']]
plt.bar(kind,data)
plt.show()
