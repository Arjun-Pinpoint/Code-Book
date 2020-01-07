# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:14:39 2019

@author: Arjun
"""

n=input()
try:
    n=int(n)
    count=1
    for i in range(1,n+1):
        count=count*i
    
    print(count)
except:
    print("Invalid Input")
