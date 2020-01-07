# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:40:17 2019

@author: Arjun
"""

l,b,h=input().split()
l=int(l)
b=int(b)
h=int(h)

area=(2*l*b)+(2*l*h)+(2*b*h)
volume=l*b*h
print(area,volume)
