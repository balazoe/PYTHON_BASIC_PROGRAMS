# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:56:02 2023

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
for i in b:
    print("Name:",i[0])
    print("College:",i[1])
    print("Degree:",i[2])
