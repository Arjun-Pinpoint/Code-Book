# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""


m,n=input().split()
m=int(m)
n=int(n)
while n!=0:
    m,n=n,m%n
print(m)
    
