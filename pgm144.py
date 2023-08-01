# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:41:08 2023

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
print(b)
