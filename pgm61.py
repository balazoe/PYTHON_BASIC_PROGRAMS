# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:25:48 2023
Biggest of 3 numbers using ternary expression
@author: Dell
"""

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=a if a<b else b
print(d)
e=c if c<d else d
print(e)