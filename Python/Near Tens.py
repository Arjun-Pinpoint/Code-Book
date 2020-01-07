# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""

n=int(input())
try:
    if n<10:
        print("10")
    else:
        ten=n//10
        ten=(ten+1)*10
        print(ten)
        
                
except:
    print("Invalid Input")
