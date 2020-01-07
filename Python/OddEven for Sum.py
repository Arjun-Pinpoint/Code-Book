# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""

m,n=input().split()
try:
    m=int(m)
    n=int(n)
    o=m-n
    
    if o%2==0:
        print("even")
    else:
        print("odd")
        
                
except:
    print("Invalid Input")
