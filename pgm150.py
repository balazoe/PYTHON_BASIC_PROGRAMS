# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:25:36 2023

@author: Dell
"""

i = 0
a1 = []
n = int(input('Enter n: '))
while i < n:
    a = []
    i1 = 0
    while i1 < n:
        d = int(input('Enter d: '))
        a.append(d)
        i1 += 1
    a1.append(a)
    i=i+1
i2 = 0
b1 = []
n = int(input('Enter n: '))
while i2 < n:
    b = []
    i4 = 0
    while i4 < n:
        d1 = int(input('Enter d1: '))
        b.append(d1)
        i4=i4+1
    b1.append(b)
    i2 += 1
i = 0
e1 = []
while i < n:
    e = []
    j = 0
    while j < n:
        z = a1[i][j] - b1[i][j]
        e.append(z)
        j=j+1
    e1.append(e)
    i=i+1
i = 0
while i < n:
    j = 0
    while j < n:
        print(e1[i][j], end=' ')
        j=j+1
    print()
    i=i+1