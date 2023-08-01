# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 19:06:16 2023

@author: Dell
"""

a = int(input("Enter a:"))
b = int(input("Enter b:"))
for i in range(a,b):
    d1=i%4
    if d1==0:
        print(i,"Leap Year")
    else:
        print(i,"not a Leap Year")