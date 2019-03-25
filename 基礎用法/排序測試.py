# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:13:42 2018

@author: Home love

顛倒排序reverse()
#可以用[::-1]方式取得串列顛倒排序

"""


food=['apple','banana','tomato','tiramizu','strawberry']
print('冰箱內的食物由左至右擺放=\n',food)
#用顛倒排序[::-1]顛倒排序內容，不更改串列內容
print('冰箱內的食物由右至左擺放=\n',food[::-1])
#更改串列內容
food.reverse()
print('從由左至右改成由右至左的擺放內容=',food)

