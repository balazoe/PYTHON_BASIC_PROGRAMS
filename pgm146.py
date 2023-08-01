# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:36:24 2023

@author: Dell
"""

i = 0
b = []
n = int(input('enter n:'))

while i<n:
    a = []
    i1 = 0
    while i1<n:
        d = int(input('enter d:'))
        a.append(d)
        i1 += 1
    b.append(a)
    i += 1

i = 0
while i<n:
    j = 0
    while j < n:
        print(b[i][j], end=' ')  
        j += 1
    print()
    i += 1