# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:24:33 2018

@author: Home love

#下載特定網址資料
import urllib.request as req
with req.urlopen(url) as response:
     data=response.read()
print(data)

"""
#import urllib.request as req
#url="https://www.ntu.edu.tw/"
#with req.urlopen(url) as response:
#     data=response.read().decode("utf-8")#讀取網頁原始碼 (HTML CSS JS)
#print(data)

##############################################################################
import urllib.request as req
import json
url="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with req.urlopen(url) as response:
     data=json.load(response) #利用json模組處理json格式
#print(data)
#取得公司名稱,將公司名稱列表出來
clist=data['result']['results']
#print(clist)
with open("內湖科技園區廠商.csv","w",encoding="utf-8") as file:
     for company in clist:
#         print(company['_id'])
#         print(company['ADDR_X'])
#         print(company['ADDR_Y'])
          file.write(company['公司名稱']+"\n")
#         print(company['\ufeff統編'])
#         print(company['公司地址'])