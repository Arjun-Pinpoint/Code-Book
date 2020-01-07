# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:11:56 2019

@author: Arjun
"""
import re
n=input()
c=0
for i in n:
    if re.match("^[.,@_!#$%^&*()<>?/\|}{~:]*$",i):
                   c+=1
print(c)
