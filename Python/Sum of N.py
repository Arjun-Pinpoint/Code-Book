# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
n=input()
try:
    n=int(n)
    add=0
    for i in range(1,n+1):
        add+=i
    print(add)
        
                
except:
    print("Invalid Input")
