# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:04:27 2019

@author: Home love
"""

import requests 
from bs4 import BeautifulSoup
import scrapy as sc

#rs=requests.get(url)
#rs.encoding='utf-8'
#soup=BeautifulSoup(rs.text,'html.parser')

#print(soup)

class ComicDownload():
     name = 'OnePiece'
     def getallpath():
          urls=('http://dmeden.net/comicinfo/170.html')
          rs = requests.get(urls)
          res = BeautifulSoup(rs.text,'lxml')
          links = res.find_all('a')
          for link in links:
               linkss=link.get('href')
               full_path = 'http://dmeden.net'+linkss
               print(full_path)
               yield sc.Request(full_path, self.parse_detail)
     def parse_detail(self, response):
          res = BeautifulSoup(response.body)
          print (res.select('#img7652').test)
     

ComicDownload.getallpath()
#ComicDownload.parse_detail()