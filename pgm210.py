# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:08:30 2023

@author: Dell
"""

s1=input()
x=s1[: : -1]
print(x)
if x==s1:
    print('palindrome')
else:
    print('not')