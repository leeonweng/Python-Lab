# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:56:06 2018

@author: Home love
"""

year=int(input("年：\n"))
month=int(input("月：\n"))
day=int(input("日：\n"))
months1=[0,31,60,91,121,152,182,213,244,274,305,335,366] #閏年
months2=[0,31,59,90,120,151,181,212,243,273,304,334,365] #平年

if ((year%4==0)and(year%100!=0)) or((year%100==0)and(year%400==0)):
    Dth=months1[month-1]+day
else:
    Dth=months2[month-1]+day
print ("是該年的第%d天"%Dth)
