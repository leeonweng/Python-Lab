# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 23:07:23 2018

@author: Home love
"""


import requests
from bs4 import BeautifulSoup
res = requests.get('https://olis.ncue.edu.tw/sp.asp?xdurl=mp1ap/ExFileList.asp&classtype=1&coll_xitem=6&dept_xitem=5&mp=1')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,"lxml")
tt=soup.find_all('a')
for ink in tt :
    tt2 = ink.get('href')
    full_path='https://olis.ncue.edu.tw/'
    if (tt2 == None or tt2.split('.')[-1] !='pdf'):
        continue
    if (tt2 [0:4]=='http'):
        fullpath = tt2
    elif(tt2[0]=='/'):
        fullpath = 'https://olis.ncue.edu.tw' + tt2
    else:
        fullpath ='https://olis.ncue.edu.tw/' + tt2
    print(fullpath)