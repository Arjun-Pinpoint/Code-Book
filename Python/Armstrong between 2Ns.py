# -*- coding: utf-8 -*-
"""
Created on Tue May 21 08:48:44 2019

@author: Arjun
"""

x,y=input().split()

try:
    x=int(x)
    y=int(y)
    for n in range(x,y):
        temp=n
        a=0
        c=0
        while(n>0):
           a=n%10
           n=n//10
           c+=a*a*a
        if temp==c:
            print(temp,end=" ")
except:
    print("Invalid Input")
