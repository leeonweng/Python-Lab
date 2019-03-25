# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:49:01 2018

@author: Home love

"""

#亂數模組
import random
#隨機選取
#從列表中隨機選取1個資料
data=random.choice([0,1,5,8,10,20])
print(data)
#從列表中隨機選取2個資料
data=random.sample([0,1,5,8,10,20,45],3)
print(data)
#將列表的資料「就地」隨機調換順序
data=[0,1,5,8]
random.shuffle(data)
print(data)
#############################################################################

#隨機亂數
import random
#取得0.0~1.0之間的隨機亂數
data=random.random()
print(data)
#同上 取得0.0~1.0之間的隨機亂數 機率皆相等
data=random.uniform(0.0,1.0)
print(data)

#############################################################################
#常態分配亂數
#取得平均數100,標準差10的常態分配亂數
data=random.normalvariate(100,10)
print(data)

data=random.normalvariate(0,5)
print(data)

#############################################################################
#統計模組
import statistics as st
mn=st.mean([1,4,6,9,10]) #平均數
med=st.median([1,4,6,9,10]) #中位數
std=st.stdev([1,4,6,9,10]) #標準差
print(mn,med,std)

#############################################################################
#繪圖範例
import matplotlib.pyplot as plt
data = [35,15,85,35,20]
plt.bar(range(len(data)),data)
plt.show()
