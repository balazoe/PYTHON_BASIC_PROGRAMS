# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 18:36:32 2023

@author: Dell
"""

s1=input('ENTER STRING:')
s2=""
n1=len(s1)
i=n1-1
while i>-1:
    s2=s2+s1[i]
    i=i-1
print(s2)
if s2==s1:
    print('palindrome')
else:
    print('not')