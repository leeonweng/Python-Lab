
import requests as req
import os
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
#from urlparse import urljoin

url = 'http://exam.lib.ntu.edu.tw/exam/graduate/term/299%20177%20175%20176%20178'
html = req.get(url)
html.encoding='utf-8'
sp=bs(html.text,"html.parser")

#建立目錄
pdf_dir="pdfs1/"
if not os.path.exists(pdf_dir):
     os.mkdir(pdf_dir)

links=sp.select("a")
#print(links)
#bb = []
for link in links:
    href=link.get("href")
#    print(href)
    if ('php?file=http://140') in href:
        fullpath = href.split('=')[1]
        paths = fullpath.split('&')[-2]
#        print(path)
    else:
        not print
        
    try:
         filename = paths.split('/')[-1]
         pdf = urlopen(paths)
         f = open(os.path.join(pdf_dir,filename),'wb')
         f.write(pdf.read())
         f.close()
    except:
         print ("{} 無法讀取!".format(filename))
         