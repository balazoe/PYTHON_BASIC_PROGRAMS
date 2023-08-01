# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 19:35:03 2023
the vowels of the string
@author: Dell
"""

s = 'linsoft academy'
i=0
while i<len(s):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        print(s[i])
    else:
        print('not')
    i=i+1