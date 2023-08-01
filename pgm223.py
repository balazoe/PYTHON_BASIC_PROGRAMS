# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:20:42 2023

@author: Dell
"""

a=[]
n=int(input("enter n:"))
for i in range(n):
    d=int(input("enter d:"))
    a.append(d)
b=0
c=555
p1=0
p2=0
for i in range(len(a)):
    if a[i]>b:
        b=a[i]
        p1=i
    elif a[i]<d:
        d=a[i]
        p2=i
a[p1]=d
a[p2]=b
print(a)