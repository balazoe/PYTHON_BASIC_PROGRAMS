# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:16:43 2023

@author: Dell
"""

i=0
b=[]
n=int(input('Enter n:'))
while i<n:
    Name = input('Enter Name:')
    College = input('Enter College:')
    Degree = input('Enter Degree:')
    a = [Name,College,Degree]
    b.append(a)
    i=i+1
print(b)
