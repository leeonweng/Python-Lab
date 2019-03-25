# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:52:53 2018

@author: Home love

#建立類別
class 類別名稱:
     定義封裝的變數
     定義封裝的函式
     
#使用類別
類別名稱.屬性名稱
"""

#定義Test類別
class Test:
     x=3 #定義變數
     def say(): #定義函式
          print('Hello')
          
#############################################################################
#定義test類別
class test:
     x=3
     def say():
          print("Hello")
#使用test類別         
test.x+3 #取得屬性x的資料3
test.say() #呼叫屬性say函式

#############################################################################
#定義類別、與類別屬性(封裝在類別中的變數與函式
#定義一個類別IO,有兩個屬性 supportedSrcs 和 read
class IO:
     supportesSrcs=['console','file']
     def read(src):
          print("Read from",src)
          
print(IO.supportesSrcs)
IO.read("file")