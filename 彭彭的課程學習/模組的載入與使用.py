# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:55:39 2018

@author: Home love
模組的使用
"""
import sys
sys.path.append("python") #再模組的搜尋路徑列表中「新增路徑」
print(sys.platform)
print(sys.maxsize)
print(sys.path)


import geometry as gt
rs=gt.distance(1,1,5,5)
print(rs)
rs=gt.slope(1,2,5,6)
print(rs)

