# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

n=int(input())
unorder=input().split()
order=sorted(unorder)
for i in range(n):
    if order[i]!=unorder[i]:
        print(i)
