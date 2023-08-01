# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:33:23 2023

@author: Dell
"""

s1=input('ENTER STRING:')
s2=""
n=int(input('ENTER n:'))
m=int(input('ENTER m:'))
for i in range(m,m+n):
    s2=s2+s1[i]
print(s2)