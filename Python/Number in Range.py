# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:09:40 2019

@author: Arjun
"""
n=input()
try:
    arr=[0,1,2,3,4,5,6,7,8,9]
    n=int(n)
    if n in arr:
        print("yes")
    else:
        print("no")
    
except:
    print("Invalid Input")
