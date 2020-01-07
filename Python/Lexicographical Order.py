# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

x=str(input())
lst=[]
for i in x:
    lst.append(i)

lst.sort()
for i in lst:
    print(i,end="")
