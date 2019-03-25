# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:22:57 2018

@author: Home love
"""
import requests
import json
import csv
from urllib.parse import urlencode
import time

def saveHtml(file_name,file_content):#儲存conten對象為html檔案
     with open(file_name.replace('/','_')+'.html','wb') as f:
          f.write(file_content)

def GetData(url,writer):#解析並將資料儲存為CSV檔案
     response= requests.get(url)
     data=response.content
     saveHtml('zlzp',data) #儲存html檔案
     jsondata=json.loads(data)
     dataList=jsondata['data']['results']
     #print(jsondata)
     for dic in dataList:
          jobName=dic['jobName'] #崗位名稱
          company=dic['company']['name'] #公司名稱
          salary=dic['salary'] #薪水
          city=dic['city']['display'] #城市
          jobtype = dic['jobType']['display'] #所屬行業
          eduLevel=dic['eduLevel']['name'] #學歷要求
          workingExp=dic['workingExp']['name'] #工作經驗
          print(jobName,company,salary,city,jobtype,eduLevel,workingExp)          
          writer.writerow([jobName,company,salary,city,jobtype,eduLevel,workingExp])

param={ 'start':0,
       'pageSize':60,
       'cityId':489,
       'workExperience':-1,
       'education':-1,
       'companyType': -1,
       'employmentType': -1,
       'jobWelfareTag': -1,
       'kw': 'BI工程師', #搜尋關鍵詞，可以根據你需要爬取的崗位信息進行更換
       'kt': 3,
       'lastUrlQuery': {"p":1,"pageSize":"60","jl":"681","kw":"python","kt":"3"}
       }#參數配置

pages=range(1,31)#爬取1-30頁資料
out_f = open('test.csv', 'w', newline="")
writer = csv.writer(out_f)
writer.writerow(['jobName','company','salary','city','jobtype','eduLevel','workingExp'])
for p in pages: #自動翻頁
     param['start']=(p-1)*60
     param['lastUrlQuery']['p']=p
     
url = 'https://fe-api.zhaopin.com/c/i/sou?' + urlencode(param)
GetData(url,writer)
time.sleep(3)#間隔休眠3秒，防止IP被封
print(p)
out_f.close()