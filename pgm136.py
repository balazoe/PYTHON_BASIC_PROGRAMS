# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:32:04 2023

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
    else:
        print('not')
    i=i+1
print(b)