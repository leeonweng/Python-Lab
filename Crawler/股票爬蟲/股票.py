# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 21:53:33 2019

@author: Home love
"""

import requests
from io import StringIO
import pandas as pd
import numpy as np

#m = input('請輸入日期(yyyy/mm/dd):\n')

#datestr = str(m)


datestr ='20190306'

# 下載股價
r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')

# 整理資料，變成表格
df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
                                     for i in r.text.split('\n') 
                                     if len(i.split('",')) == 17 and i[0] != '='])), header=0)