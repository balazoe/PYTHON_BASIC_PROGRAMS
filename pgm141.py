# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:57:02 2023

@author: Dell
"""

a=[]
n=int(input("enter n:"))
i=0
while i<n:
    d=int(input("enter d:"))
    a.append(d)
    i=i+1
i=0
b=0
d=5
p1=0
p2=0
while i<len(a):
    if a[i]>b:
        b=a[i]
        p1=i
    elif a[i]<d:
        d=a[i]
        p2=i
    else:
        print('not')
    i=i+1
a[p1]=d
a[p2]=b
print(a)