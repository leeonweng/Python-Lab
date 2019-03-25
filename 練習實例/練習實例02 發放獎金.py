# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:15:08 2018

@author: Home love
"""

def get_reward(I):
    rewards = 0
    if I <= 10 :
         rewards = I * 0.1 
      
    elif (I>10)and(I<=20):
         rewards = ( I - 10 ) * 0.075 + get_reward ( 10 )          

    elif ( I > 20 ) and ( I <= 40 ): 
         rewards = ( I - 20 ) * 0.05 + get_reward ( 20 )          

    elif ( I > 40 ) and ( I <= 60 ): 
         rewards = ( I - 40 ) * 0.03 + get_reward ( 40 )          

    elif ( I > 60 ) and ( I <= 100 ): 
         rewards = ( I - 60 ) * 0.015 + get_reward ( 60 )          

    else : 
         rewards = get_reward ( 100 ) + ( I - 100 ) * 0.01     

    return rewards

if __name__ == '__main__' : 
    i = 120000 
    print ( "淨利潤:" , i ) 
    print ( "發放的獎金為：" , get_reward ( i / 10000 ) * 10000 )
    
    
##########################################################################
