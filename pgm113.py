# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:05:44 2023

@author: Dell
"""

s = input("enter s: ")
a=b=c=d=0
i=0
while i<len(s):
    if s[i]>='A' and s[i]<='Z':
        a=a+1
    elif s[i]>='a' and s[i]<='z':
        b=b+1
    elif s[i]>='0' and s[i]<='9':
        c=c+1
    else:
        d=d+1
    i=i+1
print(a)
print(b)
print(c)
print(d)