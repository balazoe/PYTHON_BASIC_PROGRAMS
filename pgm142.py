# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:57:56 2023

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
while i<len(a):
    if a[i]>b:
        b=a[i]
        c=i
    else:
        print('not')
    i=i+1
i=0
b1=0
while i<len(a):
    if a[i]>b1 and a[i]!=b:
        b1=a[i]
        c1=i
    else:
        print('not')
    i=i+1
print(c1)