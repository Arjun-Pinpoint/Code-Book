# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

A,B,C=input().split()
a=int(A)
d=int(B)
n=int(C)

sum=0
c=0
while n>c:
    sum+=a
    a+=d
    c+=1
print(sum)
