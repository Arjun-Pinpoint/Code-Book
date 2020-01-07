# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:41:58 2019
@author: Arjun
"""

n=input()
ln=len(n)
f=0
for i in range(ln):
    if n[i]!=n[ln-i-1]:
        f=1
        break
if f==0:
    print("yes")
else:
    print("no")
