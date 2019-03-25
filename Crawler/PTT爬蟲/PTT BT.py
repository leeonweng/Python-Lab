# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:57:45 2018

@author: Home love
"""

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import os

def GetWeb(target):
     html = requests.get(target)
     soup = BeautifulSoup(html.text,'html.parser')
     article_link = soup.select('div.title a')
     article_date = soup.select('div.date')
     return soup.article_link,article_date

def Download (article_link,article_date,date):
     reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')
     
     for art,art_date in zip(article_date,article_link):
          if art_date.text == date:
               print (art['href'],art.text)
               html_article = requests.get('https://www.ptt.cc'+art['href'])
               images = reg_imgur_file.findall(html_article.text)
               path = 'D:/Python/Beauty/'+art.text
               os.mkdir(path)
               
               for image in set(images):
                    ID = re.search('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif))',image).group(1)
                    print(ID)
                    urlretrieve(image,path+'\\'+ID)
                    
def LastPage(soup):
     paging = soup.select('div.btn-group-paging a')
     pagingLast = paging[1]['href']
     url_last ='https://www.ptt.cc'+pagingLast
     target = url_last
     return target