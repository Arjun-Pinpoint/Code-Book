# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:37:53 2019

@author: Arjun
"""
lst=['a','e','i','o','u','A','E','I','O','U']
x=input()
if x in lst:
    print("Vowel")
elif x.isalpha():
    print("Consonant")
else:
    print("invalid")
