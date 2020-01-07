# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
n=input()
try:
    n=str(n)
    
    add=0
    for i in n:
        i=int(i)
        add+=i
    print(add)
except:
    print("Invalid Input")
