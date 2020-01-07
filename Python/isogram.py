# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""


x=input()

lst=[]
f=0
for i in x:
   if i in lst:
       f=1
       break
   else:
       lst.append(i)
if f==0:
    print("Yes")
else:
    print("No")
