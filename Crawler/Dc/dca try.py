# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 11:32:58 2018

@author: Home love
"""

import requests
#import os
from bs4 import BeautifulSoup
#from urllib.request import urlopen
#from urllib.request import Request
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
}
url = ('https://www.dcard.tw/f/sex')

def gethref(url):
    res = requests.get(url , headers = headers)
    soup = BeautifulSoup(res.text, "html.parser")
        
    imgs = soup.select('a')
    
    for img in imgs:
        imm = img.get('href')
#        print(imm)
        if (imm == None or imm.split('/')[-2] != ('p')):
            not print
            continue;
        else:
            fullpath = 'https://www.dcard.tw' + imm
            print(fullpath)

a = gethref(url)
#print(a)

def getimg(a):
    if a == None:
        not print
    else:
        re = requests.get(a, headers = headers)
        sp = BeautifulSoup(re.text, 'html.parser')

        print(sp)
    
    
print(getimg(a))
'''
    with open('./imgs/' + str(fn.split('/'))[-1], 'wb') as f:
        f.write(img.read())
'''