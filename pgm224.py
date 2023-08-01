# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:35:26 2023

@author: Dell
"""

a=[]
n=int(input("enter n:"))
for i in range(n):
    d=int(input("enter d:"))
    a.append(d)
b=0
for i in a:
    d1=i if i>b else b
b1=0
for i in range(len(a)):
    if a[i]>b1 and a[i]!=d1:
        b1=a[i]
print(b1)