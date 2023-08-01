# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:15:05 2023

@author: Dell
"""

n=int(input('enter n:'))
s1=str(n)
n1=len(s1)
x=s1[: : -1]
s2=int(x)
print(s2)
if x==s1:
    print('palindrome')
else:
    print('not')