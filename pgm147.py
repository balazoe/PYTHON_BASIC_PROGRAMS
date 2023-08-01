# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:01:22 2023

@author: Dell
"""

i=0
b=[]
n=int(input('enter n:'))
while i<n:
    a=[]
    i1=0
    while i1<n:
        d=int(input('enter d:'))
        a.append(d)
        i1=i1+1 
    b.append(a)
    i=i+1 
i=0
e=0
while i<n:
    j=0
    while j<len(b):
        e=e+b[i][j]
        j=j+1
    i=i+1 
print(e)
