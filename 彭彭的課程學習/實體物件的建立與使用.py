# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:24:59 2018

@author: Home love

實體物件
透過類別建立
先定義類別,再透過類別建立實體物件
建立>使用

class 類別名稱:
     #定義初始化函式
     def __init__(self):
          透過操作self來定義實體屬性
#建立實體物件,放入變數obj中
obj=類別名稱()
"""
class Point:
     def __init__(self):
          self.x=3
          self.y=4
#建立實體物件
#此實體物件包含x和y兩個實體屬性
#建立第一個實體物件
p1=Point()
print(p1.x ,p1.y)
#建立第二個實體物件

p2=Point()
print(p2.x, p2.y)

##############################################################################
class Point:
     def __init__(self,x,y):
          self.x=x
          self.y=y
#建立實體物件
#建立時,可直接傳入參數資料
p1=Point(1,5)
#建立實體物件,並取得實體屬性資料 
print(p1.x+p1.y)

p2=Point(5,8)
print(p2.x+p2.y)

##############################################################################
#FullName 實體物件的設計: 分開紀錄姓、名資料的全名
class FullName:
     def __init__(self,first,last):
          self.first=first
          self.last=last
name1=FullName('L.W','Weng')
name2=FullName('P.S','Sung')
print(name1.first,name1.last)
print(name2.first,name2.last)

##############################################################################
#實體方法
"""
#基本語法
class 類別名稱:
     #定義初始化函式
     def __init__(self):
          透過操作self來定義實體屬性
#     定義實體方法/函式
     def 方法名稱(self,更多自訂參數):
          方法主體,透過self操作實體物件
#建立實體物件,放入變數obj中
obj=類別名稱()
"""

class Point:
     def __init__(self,x,y):
          self.x=x
          self.y=y
     def show(self):
          print(self.x,self.y)
p=Point(1,5)
p.show()

##############################################################################
class Point:
     def __init__(self,x,y):
          self.x=x
          self.y=y
     #定義實體方法
     def show(self):
          print(self.x,self.y)
     def distance(self,targetX,targetY):
          return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
          
p=Point(3,4)
p.show() #呼叫實體方法 / 函式
result=p.distance(0,0) #計算座標3,4合作標0,0之間的距離
print(result)

##############################################################################
class File:
     def __init__(self,name):
          self.name=name
          self.file=None #尚未開啟檔案:初期室None
     #定義實體方法
     def open(self):
          self.file=open(self.name, mode="r", encoding="utf-8")
     def read(self):
          return self.file.read()
#讀取第一個檔案          
f1=File('data1.txt')
f1.open()
data=f1.read()
print(data)
#讀取第二個檔案
f2=File('data2.txt')
f2.open()
data=f2.read()
print(data)