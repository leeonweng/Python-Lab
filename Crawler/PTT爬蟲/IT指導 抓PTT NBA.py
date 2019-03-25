# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 21:59:19 2018

@author: Home love
"""

import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/NBA/index.html"

print('資料讀取中...')

def get_NBA(url):
    r = requests.get(url)
    sp = BeautifulSoup(r.text,"html.parser")
    rs = sp.select('.r-ent')
    # with會自動關閉檔案
    # a+模式可讀可寫，檔案不存在則創建一個，檔案存在會附加在後面
    with open('NBA try.txt', 'a+') as f:
        for item in rs:
#            f.write(item.select('.date')[0].text)
#            f.write(item.select('.nrec')[0].text)
#            f.write(item.select('.author')[0].text)
            f.write(item.select('.title')[0].text)   
            f.write('===============================')

for page in range(0,4):
    r = requests.get(url)
    sp = BeautifulSoup(r.text,"html.parser")
    btn = sp.select('div.btn-group > a')
    up_page_href = btn[3]['href']
    next_page_url = 'https://www.ptt.cc' + up_page_href
    url = next_page_url
    get_NBA(url = url)
    
if get_NBA:
     print('成功!')
else:
     print('讀取失敗!')
     