# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:33:28 2023

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
e=0
for i in b:
    for j in i:
        e+=j
print(e)