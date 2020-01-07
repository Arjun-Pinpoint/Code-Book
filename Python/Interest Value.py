# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

p,t,r=input().split()

p=int(p)
t=int(t)
r=int(r)/100

print(abs(int(p-(p*(1+(t*r))))))
