# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:59:37 2023

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
i=0
while i<n:
    print("Name:",b[i][0])
    print("College:",b[i][1])
    print("Degree:",b[i][2])
    i=i+1