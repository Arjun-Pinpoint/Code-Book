# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""

n=input()
try:
    n=str(n)
    
    binary=['0','1']
    
    f=0
    for i in n:
        if i not in binary:
            f=1
            break
    if f==1:
        print("no")
    else:
        print("yes")
        
                
except:
    print("Invalid Input")
