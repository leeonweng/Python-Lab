# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:12:43 2018

@author: Home love
"""

t = [] 
for m in range ( 168 ):
     for n in range ( m ):
          if m**2-n**2==168:
            x=n**2-100
            t.append(x) 
            print('符合條件的整數有：',t)
            
######################################################################

for i in range ( 1 , 17 ):
     for x in range ( 1 , 168 ):
          if 168 - ( i ** 2 + 2 * x * i ) == 0 :
               print (x ** 2 - 100) 
               
######################################################################
               
for i in range(1,85):
     if 168 %i == 0:
         j = 168/i;
         if i > j and ( i + j ) % 2 == 0 and ( i - j ) % 2 == 0 :
             m =( i + j ) / 2 
             n = ( i - j ) / 2 
             x = n * n - 100 
             print (x)
             
######################################################################
             
for m in range ( 168 ):
     for n in range ( m ):
          if ( m + n )*( m - n )== 168 :
               x = n ** 2 - 100
               print ("符合條件的整數有:" , x)
               
######################################################################
               
print ([ n ** 2 - 100 for m in range ( 168 ) for n in range ( m ) if ( m + n )*( m - n )== 168 ]) 