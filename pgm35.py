# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:48:55 2023
Biggest 3 Integer number
@author: Dell
"""
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
if a>b:
    if a>c:
        print("a")
    else:    
        print("c")
else:
    if b>c:
        print("b")
    else:
        print("c")
