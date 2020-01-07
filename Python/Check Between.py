# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
x=int(input())
m,n=input().split()
try:
    m=int(m)
    n=int(n)
    
    if x>m and x<n:
        print("yes")
    else:
        print("no")
        
                
except:
    print("Invalid Input")
