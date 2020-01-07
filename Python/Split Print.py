# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
n=input()
try:
    n=str(n)
    for i in n:
        print(i, end=" ")
    
except:
    print("Invalid Input")
