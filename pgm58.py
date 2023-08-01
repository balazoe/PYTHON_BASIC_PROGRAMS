# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:56:28 2023
using implicit and not operator leap year or not
@author: Dell
"""
a=int(input("Enter a"))
d1=a%4
if not d1:
    print("Leap yaer")
else:
    print("not")
