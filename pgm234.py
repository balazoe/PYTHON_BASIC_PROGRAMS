# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:48:18 2023

@author: Dell
"""

b=[]
n=int(input('Enter n:'))
for i in range(n):
    Name = input('Enter Name:')
    College = input('Enter College:')
    Degree = input('Enter Degree:')
    a = [Name,College,Degree]
    b.append(a)
for i2 in b:
    print(i2)