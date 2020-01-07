# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""

lst=['a','e','i','o','u','A','E','I','O','U']
x=str(input())
f=0
for i in x:
    if i in lst:
        f=1
        break
if f==1:
    print("yes")
else:
    print("no")
