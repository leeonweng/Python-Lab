# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:29:25 2018

@author: Home love
"""
#############################################################################
for i in range ( 1 , 5 ) :
     for j in range ( 1 , 5 ) :
         for k in range ( 1 , 5 ) :
             if ( i != k ) and ( i != j ) and ( j != k ) :
                 print(i , j , k)
                
#############################################################################
                 
list_num=[ 1 , 2 , 3 , 4 ] 
list=[ i * 100 + j * 10 + k 
      for i in list_num
      for j in list_num 
      for k in list_num 
      if ( j != i and k != j and k != i )]    
print(list)

#############################################################################

num =[ 1 , 2 , 3 , 4 ] 
i = 0 
for a in num :
     for b in num :
          for c in num :
               if ( a != b ) and ( b != c ) and ( c != a ) :
                    i += 1 
                    print( a , b , c )
print ('總數是：' , i ) 

#############################################################################

import pprint

list_num =[ '1' , '2' , '3' , '4' ] 
list_result =[] 
for i in list_num :
     for j in list_num :
          for k in list_num :
               if len ( set ( i + j + k )) == 3 :
                    list_result +=[ int ( i + j + k )] 
                    print ("能組成%d個互不相同且無重複數字的三位數: " % len ( list_result )) 
pprint . pprint ( list_result )

#############################################################################

from itertools import permutations

for i in permutations ([ 1 , 2 , 3 , 4 ], 3 ):
     print(i)    
     
############################################################################# 
     
from itertools import permutations
t = 0 
for i in permutations ( '1234' , 3 ):
     print ( '' . join ( i )) 
     t += 1 
print ( "不重複的數量有:%s" % t )