# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""

n=str(input())
x=""
for i in n:
    i=int(i)
    if i%2!=0:
        x+=str(i)
        x+=" "

for i in range(len(x)-1):
    print(x[i],end="")
