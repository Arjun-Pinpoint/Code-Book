# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""


try:
    m,n=input().split()
    m=int(m)
    n=int(n)
    range=2**32
    if m<range and n<range:
        print(abs(m-n))
    else:
        print("Number should be less than 2^32")
except:
    print("Invalid")
