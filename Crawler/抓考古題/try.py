# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:53:24 2019

@author: User
"""

import requests as req
import os
from bs4 import BeautifulSoup as bfs
from urllib.request import urlopen
import json

url = 'https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=zh-TW&source=gcsc&gss=.com&cx=015041549054067603329:lhirb15e2dk&q=%E5%BF%83%E7%90%86%E6%B8%AC%E9%A9%97%E5%93%A1&safe=off&cse_tok=AKaTTZheDzYU0cMvRPPAcXHpBuu6:1552826972056&exp=csqr&callback=google.search.cse.api19041'
re = req.get(url)
re.encoding = 'uft-8'
jdoc = json.load(re.text)
print(jdoc)[0]

'''
sp = bfs(re.text,'html.parser')
print(sp)
df = sp.select('a')

for src in df:
    href = src.get('href')
    print(href)
    
'''


a = ['9億楓幣=100元【1:900萬】【光速】安全★快速★可靠★幫開百元散單★最高比值〓24H營業★楓幣來源拍賣',
     '10億楓幣=100元【1:100萬】【台灣人自售】【火速移交】【絕無BUG幣】【絕非大陸工作室】',
     '10.8億楓幣=100元【1:100萬】「鳳姐專賣」人在可提問~可開非整數~自由市場6頻交易喲~認準保字會員~安全可靠喲']
for aa in a[:]:
#    print(aa)
    if aa[4] == ('='):
        print(aa)
    elif aa[5] == ('='):
        print(aa)
    elif aa[6] == ('='):
        print(aa)
    elif aa[7] == ('='):
        print(aa)
    else:
        not print

print(a)
if a[4] == ('='):
    print(a)
elif a[5] == ('='):
    print(a)
else:
    not print
