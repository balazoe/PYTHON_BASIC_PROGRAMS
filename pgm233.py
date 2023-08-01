# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:46:22 2023

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
print(b)