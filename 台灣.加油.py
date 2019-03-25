# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 23:00:48 2019

@author: Home love
"""

from __future__ import print_function
 
class 主權獨立的國家:
    def __init__(self): 
        self.國名='中華民國'
        self.實名='台灣'
        self.別名='福爾摩沙'
 
    def 加油(self):
        self._反對 ='一國兩制'
        self._人民 = '絕大多數台灣民意'
        self._贊成 = '台灣共識'
        return self
 
    def __repr__(self):
        return ('台灣絕不會接受「{0}」，\n'+
                '{1}也堅決反對「{0}」，\n'+
                '而這也是【{2}】。').format(self._反對, self._人民, self._贊成)

if __name__ == '__main__':
    
    台灣 = 主權獨立的國家()
    print(台灣.加油())