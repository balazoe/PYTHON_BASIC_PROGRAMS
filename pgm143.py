# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:01:11 2023

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
c=0
c1=0
while i<len(a):
    if a[i]>b:
        b=a[i]
        c=i
    elif a[i]<d:
        d=a[i]
        c1=i
    else:
        print('not')
    i=i+1
i=0
b1=0
d1=4
p1=0
p2=0
while i<len(a):
    if a[i]>b1 and a[i]!=b:
        b1=a[i]
        p1=i
    elif a[i]<d1 and a[i]!=d:
        d1=a[i]
        p2=i
    else:
        print('not')
    i=i+1
a[p1]=d1
a[p2]=b1
print(a)