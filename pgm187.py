# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:49:17 2023

@author: Dell
"""

s = input('enter s:')
for i in range(len(s)):
    if s[i] in 'aeiou':
        print(s[i],end='')