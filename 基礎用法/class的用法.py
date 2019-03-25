# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:53:07 2018

@author: Home love
"""

"""
class Animal():
     def __init__(self, name):
          self.name = name

a = Animal("dog")  #建立一個名叫dog的Animal實體(物件)
print(a.name)
"""


"""

class Account:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0
        
    def deposit(self, amount):  #存款動作: amount代表存入金額
        if amount <= 0:
            raise ValueError('must be positive')
        self.balance += amount
        
    def withdraw(self, amount): #取款動作: amount代表取款金額
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError('balance not enough')
            
            
acct1 = Account('123–456–789', 'Justin') #開一個帳戶
acct1.deposit(100)
acct1.withdraw(30)
print(acct1.balance) #餘額是 70
"""
class Account:
    pass

def deposit(acct, amount):
    if amount <= 0:
        raise ValueError('must be positive')
    acct.balance += amount
       
def withdraw(acct, amount):
    if amount <= acct.balance:
        acct.balance -= amount
    else:
        raise RuntimeError('balance not enough')
        
acct = Account()
acct.number = '123-456-789'
acct.name = 'Justin'
acct.balance = 0

print(acct.number)    # 123-456-789
print(acct.name)      # Justin

deposit(acct, 100)
print(acct.balance)   # 100
withdraw(acct, 50)
print(acct.balance)   # 50
