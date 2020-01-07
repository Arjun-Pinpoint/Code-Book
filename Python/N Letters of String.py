# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
x,n=input().split()
try:
    x=str(x)
    n=int(n)
    for i in range(n):
        print(x[i],end="")
        
                
except:
    print("Invalid Input")
