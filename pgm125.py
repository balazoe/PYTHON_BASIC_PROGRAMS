# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:08:20 2023

@author: Dell
"""

n=int(input())
s2=""
s1=str(n)
n1=len(s1)
i=n1-1
while i>-1:
    s2=s2+s1[i]
    i=i-1
s3=int(s2)
print(s3)
if s2==s1:
    print('palindrome')
else:
    print('not')