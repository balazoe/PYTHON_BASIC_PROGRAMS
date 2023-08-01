# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:04:58 2023

@author: Dell
"""

b=[]
n=int(input('enter n:'))
for i in range(n):
    a=[]
    for i in range(n):
        d=int(input('enter d:'))
        a.append(d)
    b.append(a)
print(b)