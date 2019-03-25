# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:58:27 2018

@author: Home love
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://olis.ncue.edu.tw/sp.asp?xdurl=mp1ap/ExFileList.asp&classtype=1&coll_xitem=6&dept_xitem=5&mp=1")
soup = BeautifulSoup(html,"html.parser")
#print (soup.find_all("a"))
link = soup.find_all("a")
href = link.get("href")
print(href)