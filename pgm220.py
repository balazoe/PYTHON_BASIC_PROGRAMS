# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:56:31 2023

@author: Dell
"""

a=[]
n=int(input('enter n:'))
for i in range(n):
    d=int(input('enter d:'))
    a.append(d)
b=0
for i in a:
    d1=i if i>b else b
print(d1)