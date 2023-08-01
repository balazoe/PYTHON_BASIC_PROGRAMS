# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:13:31 2023

@author: Dell
"""

s = input("enter s: ")
i=0
while i<len(s):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        print(s[i])
    else:
        print('not')
    i=i+1
