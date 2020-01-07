# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

try:
    n=int(input())
    if n%2==0:
        print(int(n/2))
    else:
        print(n)
except:
    print("Invalid")      
