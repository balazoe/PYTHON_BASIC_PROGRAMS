# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:27:11 2023

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
e=0
while i<len(a):
    e=e+a[i]
    i=i+1
print(e)