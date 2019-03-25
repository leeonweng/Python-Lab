# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:58:45 2018

@author: Home love

在此模組中定義幾何運算功能

"""
#平面上兩點的距離
def distance(x1,y1,x2,y2):
     return ((x2-x1)**2+(y2-y1)**2)**0.5

#計算線段的斜率
def slope(x1,y1,x2,y2):
     return (y2-y1)/(x2-x1)