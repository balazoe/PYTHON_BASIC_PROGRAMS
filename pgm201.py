# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:08:39 2023

@author: Dell
"""

s1=input('enter s1:')
s2=""
n1=len(s1)
for i in range(-1,-n1-1,-1):
    s2=s2+s1[i]
print(s2)