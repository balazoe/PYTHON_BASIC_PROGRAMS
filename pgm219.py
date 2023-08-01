# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:44:01 2023

@author: Dell
"""

a=[]
n=int(input('enter n:'))
for i in range(n):
    d=int(input('enter d:'))
    a.append(d)
e=0
for i in a:
    e+=i
print(e)