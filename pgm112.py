# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:09:43 2023

@author: Dell
"""

s = input("enter s: ")
a=b=0
i=0
while i<len(s):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        a=a+1
    elif s[i]!='a' or s[i]!='e' or s[i]!='i' or s[i]!='o' or s[i]!='u':
        b=b+1
    else:
        print('not')
    i=i+1
print(a)
print(b)