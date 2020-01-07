# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

try:
    n,k=map(int,input().split())
    nth=input().split()
    order=sorted(nth)
    print(order[k-1])
except:
    print("Invalid")      
