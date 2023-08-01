# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 20:01:37 2023

@author: Dell
"""

a=[]
n=int(input('enter n:'))
for i in range(n):
    d=int(input('enter d:'))
    a.append(d)
b=99
for i in a:
    d1=i if i<b else b
print(d1)