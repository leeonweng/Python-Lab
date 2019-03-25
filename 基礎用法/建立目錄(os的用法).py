# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:24:57 2018

@author: Home love
"""

import os

###########################################
""" 刪除檔案
file = "myfile.txt"
if os.path.exists(file):
     os.remove(file)
else:
     print(file + "檔案未建立!")
"""     
###########################################
""" 建立目錄
dir = "file"
if not os.path.exists(dir):
     os.mkdir(dir)
else:
     print(dir + "已建立!")
"""
###########################################     
""" 刪除目錄
dir = "file"
if os.path.exists(dir):
     os.rmdir(dir)
else:
     print(dir + "目錄未建立!")
"""
###########################################
"""
cur_path=os.path.dirname(__file__) #取得目前路徑
os.system("cls") #清除螢幕
os.system("mkdir dir2") #建立dir2目錄
os.system("copy ossystem.py dir2\copyfile.py") #複製檔案
file=cur_path + "\dir2\copyfile.py"
os.system("notepad"+file) #以記事本開啟 copyfile.py 檔
"""
###########################################

cur_path=os.path.dirname(__file__)
print("現在目錄路徑:"+cur_path)

filename=os.path.abspath("ospath.py")
if os.path.exists(filename):
     print("完整路徑名稱:"+filename)
     print("檔案大小:",os.path.getsize)
     
     basename=os.path.basename(filename)
     print("最後的檔案或路徑:"+basename)
     
     dirname=os.path.dirname(filename)
     print("目前檔案目標路徑:"+dirname)
     
     print("是否為目錄:",os.path.isdir(filename))
     
     fullpath,fname=os.path.split(filename)
     print("目錄路徑:"+fullpath)
     print("檔名:"+fname)
     
     Drive,fpath=os.path.splitdrive(filename)
     print("磁碟機:"+Drive)
     print("路徑名稱:"+fpath)
     
     fullpath = os.path.join(fullpath + "\\" + fname)
     print("組合路徑=" + fullpath)
     
###########################################     
           