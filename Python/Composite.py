# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
n=int(input())


f=0
for i in range(2,n):
    if n%i==0:
        f=1
        break
        
if f==0:
    print("no")
else:
    print("yes")
