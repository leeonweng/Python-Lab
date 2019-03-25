
import requests as re
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import sys
import time
from bs4 import BeautifulSoup as bs

print('程式讀取中...請稍後!')

url ='https://www.8591.com.tw/mallList-list.html?&group=1&searchType=0&priceSort=0&ratios=0&searchGame=859&searchServer=0&firstRow=0&totalRows=459'
header ={'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

def get_soup(url):
    soups =[]
    try:
        for page in range(0,400):
            html = re.get('https://www.8591.com.tw/mallList-list.html?&group=1&searchType=0&priceSort=0&ratios=0&searchGame=859&searchServer=0&firstRow=' + str(page) + '&totalRows=459',
                          headers = header)
            if html.status_code == 200:
                sps = bs(html.text,'lxml')
                sps.encoding= 'utf-8'
                tit = sps.find_all('a')
                for ttss in tit:
                    titless = ttss.get('title')
                    if titless == None:
                        not print
                    else:
                        soups.append(titless)
                        time.sleep(2)
            else:
                print('網站無法讀取！')
        return soups
    except Exception as e:
        print(e)
        sys.exit()
        
a = get_soup(url)

def remove_index(a):
    df = []
    for remove in a:
#        print(remove)
        if ('=') not in remove:
            not print
        else:
            df.append(remove)

    return df


#print(remove_index(a))


print('資料下載中...')
xlsx_title = ['楓幣幣值','台幣','比值']
df2 = pd.DataFrame(remove_index(a), columns=xlsx_title)
time.sleep(5)


print('資料輸出中...')
df2.to_excel('8591楓幣幣值搜尋_20190319.xlsx')
time.sleep(5)

print('資料下載完成!')

#print(get_soup(url))
#df1 = pd.DataFrame(get_soup(url))
#df1.to_csv('8591楓幣幣值搜尋20190318.xlsx')