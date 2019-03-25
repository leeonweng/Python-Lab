#import requests
import os
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = ('https://tw.observer/search/%23%E8%A5%BF%E6%96%AF')
headers ={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
#opener = urllib.request.build_opener()
#opener.addheaders = [headers]
#data = opener.open(url).read()
#print(data)
req = urllib.request.Request(url, headers=headers)
rs = urllib.request.urlopen(req).read()
print(rs)
#res = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup)
imgs = soup.find_all('img',class_='small')
print(imgs)

#建立目錄
img_dir="imgs2/"
if not os.path.exists(img_dir):
     os.mkdir(img_dir)
     print('資料夾建立中…')
else:
    print(img_dir,'已建立資料夾!')
for img in imgs:
    fn = img['src']
    print(fn)
    full_path = fn
    try:
        fullname=full_path.split('/')[-1]
        img=urlopen(fn)
        f = open(os.path.join(fullname), 'wb')
        f.write(img.read())
        f.close()
    except Exception as e:
        print (e)
    continue

print('下載結束')
    
#    with open('/imgs2' + str(fn) + '.png' + '.jpg' , 'wb') as f:
#            f.write(img.read())
#            f.close()

"""
import urllib.request 
url = "http://www.oschina.net/" 
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11') 
opener = urllib.request.build_opener() 
opener.addheaders = [headers] 
data = opener.open(url).read() 
print(data)
"""