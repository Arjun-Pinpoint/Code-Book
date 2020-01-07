# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""


x=input()

a=""
b=""
c=0
for i in x:
   if c%2==0:
       a+=i
   else:
       b+=i
   c+=1
print(a+" "+b)
