# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""

x,y=input().split()
x=int(x)
y=int(y)

z=x*y

sqr=z**0.5
if sqr**2==z:
	print("yes")
else:
	print("no")
