# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

try:
    n,k=map(int,input().split())
    nth=input().split()
    c=0
    for i in nth:
        if int(i)%2!=0:
            c+=1
        if c==k:
            print(i)
            break
except:
    print("Invalid")      
