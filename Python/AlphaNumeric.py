# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:32:29 2019

@author: Arjun
"""
x=input()
try:
    alp=0
    num=0
    for i in x:
        if i.isalpha():
            alp=1
        if i.isnumeric():
            num=1
    if alp==1 and num==1:
        print("Yes")
    else:
        print("No")
                
except:
    print("Invalid Input")
