# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:27:49 2019

@author: User
"""

import requests as re
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import sys
import time
from bs4 import BeautifulSoup as bs
url ='https://www.8591.com.tw/mallList-list.html?&group=1&searchType=0&priceSort=0&ratios=0&searchGame=859&searchServer=0&firstRow=0&totalRows=459'
header ={
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

def get_soup(url):
    soups =[]
    try:
        for page in range(0,2):
            html = re.get('https://www.8591.com.tw/mallList-list.html?&group=1&searchType=0&priceSort=0&ratios=0&searchGame=859&searchServer=0&firstRow=' + str(page) + '&totalRows=459',
                         headers = header)
            if html.status_code == 200:
                sps = bs(html.text,'lxml')
                sps.encoding= 'utf-8'
                tit = sps.find_all('a')
                for ttss in tit:
                    titless = ttss.get('title')
                    print(titless)
#                    for df in titless[:]:
#                       print(df)
    except Exception as e:
        print(e)
        sys.exit()       
print(get_soup(url))                  
                        
                        if df == None:
                            not print
                        else:
                            soups.append(df)
                            time.sleep(1)
            else:
                print('Errow')
            return soups
        
    except Exception as e:
        print(e)
        sys.exit()               
print(get_soup(url))
'''
                    for df in titless[:]:
                        if df[4] == ('='):
                            print(df)
                        elif df[5] == ('='):
                            print(df)
                        elif df[6] == ('='):
                            print(df)
                        elif df[7] == ('='):
                            print(df)
                        else:
                            not print
                            time.sleep(2)

#                    if (titless == None or titless.split('=')[-1] != ('楓幣')):
#                        continue;
#                    else:
#                        soups.append(titless)
#                        time.sleep(2)
            else:
                print('網站無法讀取！')
            return soups

    except Exception as e:
        print(e)
        sys.exit()


#get_soup(url)
print(get_soup(url))
df1 = pd.DataFrame(get_soup(url))
'''