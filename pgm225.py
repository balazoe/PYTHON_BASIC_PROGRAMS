# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:53:42 2023

@author: Dell
"""

a=[]
n=int(input("enter n:"))
for i in range(n):
    d=int(input("enter d:"))
    a.append(d)
b=0
d=99
for i in range(len(a)):
    if a[i]>b:
        b=a[i]
    elif a[i]<d:
        d=a[i]
b1=0
d1=88
p1=0
p2=0
for i in range(len(a)):
    if a[i]>b1 and a[i]!=b:
        b1=a[i]
        p1=i
    elif a[i]<d1 and a[i]!=d:
        d1=a[i]
        p2=i
a[p1]=d1
a[p2]=b1
print(a)