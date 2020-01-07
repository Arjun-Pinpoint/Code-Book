# -*- coding: utf-8 -*-
"""
Created on Mon May 20 22:23:48 2019

@author: Arjun
"""

y=int(input())
if y%400==0 or y%4==0 and y%100!=0:
    print("yes")
else:
    print("no")
