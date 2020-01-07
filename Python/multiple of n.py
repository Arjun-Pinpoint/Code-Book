# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:11:56 2019

@author: Arjun
"""

n=input()
try:
    n=int(n)
    for i in range(1,6):
        print(n*i,end=" ")
except:
    print("Invalid Input")
