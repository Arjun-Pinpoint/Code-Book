# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

try:
    a,b,c=map(int,input().split())
    print(int(a*b/c))
except:
    print("Invalid")      
