# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:28:54 2019

@author: Arjun
"""

x,y=input().split()
try:
    x=int(x)
    y=int(y)
    
    x=y-x
    y-x-y
    x=y-x
    print(y,x)
     
except:
    print("Invalid Input")
