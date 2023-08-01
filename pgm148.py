# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:06:28 2023

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
c=0
while i < n:
    j = 0
    while j < n:
        if b[i][j] > c:
            c = b[i][j]
        else:
            print('not')
        j=j+1
    i=i+1
print(c)