# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:36:02 2023

@author: Dell
"""

s = 'LINSOFT ACADEMY'
for i in range(0,15):
    if s[i] not in 'AEIOU':
        print(s[i],end='')