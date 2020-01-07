# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:41:04 2019

@author: Arjun
"""

x,y=input().split()
try:
    x=int(x)
    y=int(y)
    
    x,y=y,x
    print(x,y)
     
except:
    print("Invalid Input")
