# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:12:30 2019

@author: User
"""

#藉由首頁取得所有文章的URL
import requests
from bs4 import BeautifulSoup as bs
#import json

#test = open("spider/pet/test.txt","w",encoding='UTF-8')
url = 'https://www.dcard.tw/f/pet/p/230931365-在糖廠撿到の小貓'
r = requests.get(url)
bb = bs(r.text,'lxml')
print(bb)

#p = requests.Session()

url=requests.get("https://www.dcard.tw/f/pet")
soup = bs(url.text,"html.parser")
sel = soup.select('a')
#sel = soup.select("div.PostList_wrapper_2BLUM a.PostEntry_root_V6g0r")
#print(sel)

for s in sel:
    b = s.get('href')
#    print(b)
    if b == None or b.split('/')[-2] != ('p'):
        not print
        continue;
    else:
        fullpath = "https://www.dcard.tw" + b
        print(fullpath)
        
        for o in fullpath:
            print(o)
            r = requests.get(o)
            b = bs(r.text, 'html.parser')
            g = b.find_all('a')
            print(g)
            

#print(url)
'''
a=[]
for s in sel:
    a.append(s["href"])
url = "https://www.dcard.tw"+ a[2]

for k in range(0,10):
        post_data={
            "before":a[-1][9:18],
            "limit":"30",
            "popular":"true"
        }
        r = p.get("https://www.dcard.tw/_api/forums/pet/posts",params=post_data, headers = { "Referer": "https://www.dcard.tw/", "User-Agent": "Mozilla/5.0" })
        data2 = json.loads(r.text)
        for u in range(len(data2)):
            Temporary_url = "/f/pet/p/"+ str(data2[u]["id"]) + "-" + str(data2[u]["title"].replace(" ","-"))
            a.append(Temporary_url)
j=0 #為了印頁數
q=0 #為了印張數
for i in a[2:]:
    url = "https://www.dcard.tw"+i
    j+=1
    print ("第",j,"頁的URL為:"+url)
    #file.write("temperature is {} wet is {}%\n".format(temperature, humidity))
    test.write("第 {} 頁的URL為: {} \n".format(j,url))
    url=requests.get(url)
    soup = BeautifulSoup(url.text,"html.parser")
    sel_jpg = soup.select("div.Post_content_NKEl9 div div div img.GalleryImage_image_3lGzO")
    for c in sel_jpg:
        q+=1
        print("第",q,"張:",c["src"])
        test.write("%\n""第 {} 張: {} \n".format(q,c["src"])) 
        pic=requests.get(c["src"])
        img2 = pic.content
        pic_out = open("spider/pet/"+str(q)+".png",'wb')
        pic_out.write(img2)
        pic_out.close()

test.close()
print("爬蟲結束")
'''