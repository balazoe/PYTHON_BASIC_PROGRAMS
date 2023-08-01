# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:08:58 2023

@author: Dell
"""

s = input('enter s:')
a=b=c=d=0
for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z':
        a+=1
    elif s[i]>='a' and s[i]<='z':
        b+=1
    elif s[i]>='0' and s[i]<='9':
        c+=1
    else:
        d+=1
print(a)
print(b)
print(c)
print(d)