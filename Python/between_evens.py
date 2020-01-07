# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:28:01 2019

@author: Arjun
"""

x, y= input().split()
x=int(x)
y=int(y)

for i in range(x+1,y):
    if i%2==0:
        print(i,end=" ")
