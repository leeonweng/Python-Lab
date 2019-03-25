# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:40:36 2019

@author: Home love
"""

import urllib.request  # 從網頁上將html原始碼爬下來
import re              # 進行正規表示式匹配
import pandas as pd    # 整理成最後的表格以及輸出
import time            # 每次爬取設定停止時間
import numpy as np     # 隨機設定停止時間
from bs4 import BeautifulSoup

def getHtml(url):
     try:
          page = urllib.request.urlopen(url)  # 將網頁爬取下來
          html = page.read()                  # 存原始碼到html變數中
     except:
          print("failed to geturl")           # 如果網路連線異常，則報錯。
     else:
          return html
     
def getComment(html):
     commentList = re.findall(r'<p class=""> (.*?)<', html, re.S)
     return commentList

# 匹配對電影的評分
def getScore(html):
     is_scoreList = re.findall(r'<span class="comment-info">(.*?)<span class="comment-time "', html, re.S)
     scoreList = []
     for item in is_scoreList:
          if item.count('rating') == 0:
               scoreList.append("NA")
          else:
               scoreList.append(re.findall(r'<span class="allstar(.*?)0 rating"', item, re.S))
               return scoreList

scoreList=[]
commentList=[]

for page in range(0, 220, 20):
# 爬取網頁（同前面）
     url = 'https://movie.douban.com/subject/26384741/comments?start={}&limit=20&sort=new_score&status=P&percent_type='.format(page)
     soup = BeautifulSoup(getHtml(url).decode("UTF-8"),'html.parser')
# 先初步提取內容，提取每篇短評的大框架
     tags = soup("div", {"class": "comment-item"})
for tag in tags:
# 獲取短評資訊
     comment = tag.p.getText()
# 獲取得分資訊
     try:
          score = tag.find(class_ = re.compile("star"))['class'][0]
     except:
          score = 'NA'
# 總和列表
commentList.append(comment)
scoreList.append(score)
# 設定間隔時間，並輸出迴圈爬取資訊
print(page)
time.sleep(np.random.uniform(2, 4))