# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:10:36 2023

@author: Dell
"""

s1=input()
s2=""
n=int(input())
n1=len(s1)
i=1
while i<n+1:
    s2=s2+s1[-i]
    i=i+1
print(s2)