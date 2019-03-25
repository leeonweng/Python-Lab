# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:16:27 2019

@author: liwei
"""

import requests,os
from bs4 import BeautifulSoup

class ComicDownloader():
    name='OnePiece'
#    urls=('http://dmeden.net/comicinfo/170.html')
    def getallpath():
        urls=('http://dmeden.net/comicinfo/170.html')
        rs=requests.get(urls)
        rs.encoding='utf-8'
        res=BeautifulSoup(rs.text,'html.parser')
        for link in res.find_all('a'):
            links=link.get('href')
            full_path='http://dmeden.net'+links
            print(full_path)
            yield requests(full_path)

ComicDownloader.getallpath()

comic_dir='Comic'
if not os.path.exists(comic_dir):
    os.mkdir(comic_dir)
    print('資料夾建立中…')
else:
    print(comic_dir + '資料夾已建立!')

