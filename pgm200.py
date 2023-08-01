# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:56:21 2023

@author: Dell
"""

n=int(input('enter n:'))
s2=""
s1=str(n)
n1=len(s1)
for i in range(n1-1,-1,-1):
    s2=s2+s1[i]
s3=int(s2)
print(s3)
if s3==n:
    print('palindrome')
else:
    print('not')