import requests as req
import pandas as pd
import sys
import time
import re
from bs4 import BeautifulSoup as bs

headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
           }

url = 'http://dmeden.net/comicinfo/170.html'
qq = req.get(url, headers = headers)
qq.encoding = 'utf-8'
ww = bs(qq.text, 'lxml')
rr = ww.select('a')
    
def get_name(rr):
    aaa = []
    for tt in rr:
        yy = tt.get('title')
        if yy == None:
            not print
        else:
            aaa.append(yy)
    return aaa

    bbb=[]
    for remove in aaa:
        if ('海賊王') in remove:
            bbb.append(remove)
        else:
            not print
    return bbb
        
c = get_name(rr)

def get_tophref(url):
    dff = []
    try:
        r = req.get(url, headers = headers)
        r.encoding = 'utf-8'
        s = bs(r.text, 'lxml')
        d = s.select('a')
        
        for gg in d:
            a = gg.get('href')
            if ('/comic/checkview') in a:
                n = re.sub(r'\D', '', a)
                dff.append(n[:-1])
            else:
                not print
        return dff
    except Exception as e:
        print(e)
        sys.exit()

num = get_tophref(url)

def get_sechref(num):
    df3 = []
    for i in num:
        fullpath = 'http://dmeden.net/comichtml/' + i + '/1.html?s=9'
        for page in range(1):
            if int(i)<1000:
                for pages in range(1,120):
                    fullpath = 'http://dmeden.net/comichtml/' + i + '/'+ str(pages) + '.html?s=9'
                    df3.append(fullpath)
            else:
                for pages2 in range(1,31):
                    f_path = 'http://dmeden.net/comichtml/' + i + '/'+ str(pages2) + '.html?s=9'
                    df3.append(f_path)
        return df3

a = get_sechref(num)

def get_imgname(a):
    dff2 = []
#    print(a)
    for gg in a:
#        print(gg)
        rs = req.get(gg, headers = headers)
        bss = bs(rs.text, 'lxml')
        immg = bss.select('img')
#        print(immg)
        for z in immg:
            sss = z.get('name')
#            print(sss)
            dff2.append(sss)
    return dff2
    
b = get_imgname(a)
#print(b)
df4 = pd.DataFrame(b, index=c)
df4.to_excel('One Piece.xlsx')
#time.sleep(1)