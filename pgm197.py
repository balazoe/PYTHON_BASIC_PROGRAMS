# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:35:24 2023

@author: Dell
"""

s1=input('ENTER STRING:')
s2=""
n=int(input("ENTER N:"))
n1=len(s1)
for i in range(n1-n,n1):
    s2=s2+s1[i]
print(s2)