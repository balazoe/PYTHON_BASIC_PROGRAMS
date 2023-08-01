# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:14:23 2023

@author: Dell
"""

a=[]
n=int(input("enter n:"))
for i in range(n):
    d=int(input("enter d:"))
    a.append(d)
b=0
d=199
for i in range(len(a)):
    if a[i]>b:
        b=a[i]
    elif a[i]<d:
        d=a[i]
print(b)
print(d)