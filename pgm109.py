# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:41:34 2023

@author: Dell
"""

s = 'linsoft academy'
i=0
while i<len(s):
    if s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u':
        print(s[i])
    else:
        print('not')
    i=i+1