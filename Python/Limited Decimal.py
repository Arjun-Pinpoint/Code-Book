# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""


try:
    h,w=input().split()
    h=float(h)
    w=float(w)
    a=h*w
    print("%.5f"%a)
except:
    print("Invalid")
