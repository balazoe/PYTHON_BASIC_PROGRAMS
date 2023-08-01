# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:25:48 2023
Smallest 3 integer using nested ternary expression
@author: Dell
"""

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=(a if a<c else c) if a<b else (b if b<c else c)
print(d)
