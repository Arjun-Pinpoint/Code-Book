# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
n=input()
try:
    n=int(n)
    if n%2==0:
        print(n)
    else:
        print(n-1)
except:
    print("Invalid Input")
