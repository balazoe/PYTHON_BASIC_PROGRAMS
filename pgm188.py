# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:55:00 2023

@author: Dell
"""

s = input('enter s:')
a=b=0
for i in range(len(s)):
    if s[i] in 'aeiou':
        a=a+1
    elif s[i] not in 'aeiou':
        b=b+1
print(a)
print(b)