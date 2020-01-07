# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:02:02 2019

@author: Arjun
"""

n=int(input())

f=0
for i in range(2,n-1):
    if n%i==0:
        f=1
        break
if f==0:
    print("yes")
else:
    print("no")
