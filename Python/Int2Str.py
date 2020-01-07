# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
n=input()
try:
    n=int(n)
    switcher={0:"Zero",
              1:"One",
              2:"Two",
              3:"Three",
              4:"Four",
              5:"Five",
              6:"Six",
              7:"Seven",
              8:"Eight",
              9:"Nine",
              10:"Ten"            
            }
    ret=switcher.get(n)
    print(ret)
except:
    print("Invalid Input")

