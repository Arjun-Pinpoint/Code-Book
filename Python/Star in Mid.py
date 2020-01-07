# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
x=input()

ln=len(x)
mid=ln//2

if ln%2==0:
    for i in range(ln):
        if i==mid or i==mid-1:
            print("*",end="")
        else:
            print(x[i],end="")
else:
    for i in range(ln):
        if i==mid:
            print("*",end="")
        else:
            print(x[i],end="")
        

