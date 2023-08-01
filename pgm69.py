# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:03:52 2023
uni code upper lower digit and sc
@author: Dell
"""

d1=input("enter d1")
u=ord(d1)
if u>=65 and u<=90:
    print("upper case")
elif u>=97 and u<=122:
    print("lower case")
elif u>=48 and u<=57:
    print("Digit")
else:
    print("special character")
    