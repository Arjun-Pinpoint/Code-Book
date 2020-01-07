# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:09:40 2019

@author: Arjun
"""

x,y=input().split()
try:
    x=str(x)
    y=str(y)
    
    if len(x)>len(y):
        print(x)
    else:
        print(y)
except:
    print("Invalid Input")
