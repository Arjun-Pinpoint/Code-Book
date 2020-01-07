# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:09:40 2019

@author: Arjun
"""

x,y=input().split()
try:
    x=str(x)
    y=int(y)
    
    for i in range(y):
        print(x)
except:
    print("Invalid Input")
