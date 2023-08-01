# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:25:48 2023
Smallest 3 integer number
@author: Dell
"""

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=a if a<b else b
e=c if c<d else d
print(e)
