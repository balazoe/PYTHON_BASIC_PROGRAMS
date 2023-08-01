# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:40:37 2023

@author: Dell
"""

s1=input('ENTER STRING:')
s2=""
n1=len(s1)
for i in range(n1-1,-1,-1):
    s2=s2+s1[i]
print(s2)