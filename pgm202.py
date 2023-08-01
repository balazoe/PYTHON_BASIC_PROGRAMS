# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:18:48 2023

@author: Dell
"""

s1=input('enter s1:')
s2=""
n=int(input('enter n:'))
n1=len(s1)
for i in range(-1,-n-1,-1):
    s2=s2+s1[i]
print(s2)