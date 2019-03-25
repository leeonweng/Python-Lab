# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 23:09:31 2019

@author: Home love
"""

import json

with open('11 機器學習概要.ipynb','r',encoding='utf-8') as reader:
     data = json.loads(reader.read())
     line=reader.readline()
     d = json.loads(line)
     name = d['cell_type']
     print(name)
     reader.close()
     
#print(data)
#print(name)