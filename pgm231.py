# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:57:29 2023

@author: Dell
"""

a1=[]
n=int(input('enter n:'))
for i in range(n):
    a=[]
    for i1 in range(n):
        d=int(input('enter d:'))
        a.append(d)
    a1.append(a)
b1=[]
n=int(input('enter n:'))
for i2 in range(n):
    b=[]
    for i3 in range(n):
        d1=int(input('enter d:'))
        b.append(d1)
    b1.append(b)
e1 = []
for i in range(n):
    e=[]
    for j in range(n):
        z=a1[i][j]+b1[i][j]
        e.append(z)
    e1.append(e)
for i in e1:
    for j in i:
        print(j,end=' ')
    print()
