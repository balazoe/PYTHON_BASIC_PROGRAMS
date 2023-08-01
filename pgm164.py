# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:03:50 2023

@author: Dell
"""

a = int(input("Enter a:"))
b = int(input("Enter b:"))
for i in range(a,b):
    d1=i%2
    if d1==0:
        print(i,"even number")
    else:
        print(i,"not a even number")