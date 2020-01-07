# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
m,n=input().split()
try:
    n=int(n)
    m=int(m)
    if (m*n)%2==0:
        print("even")
    else:
        print("odd")
except:
    print("Invalid Input")
