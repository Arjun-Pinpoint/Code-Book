# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

try:
    x,n=input().split()
    x=str(x)
    n=int(n)
    print(x[-n:])
except:
    print("Invalid")      
