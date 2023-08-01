# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:25:49 2023

@author: Dell
"""

a=b=e=d=0
c = input("enter c: ")
while c!='$':
    print(c)
    if c<='A' and c<='Z':
        a=a+1
    elif c<='a' and c<='z':
        b=b+1
    elif c<='0' and c<='9':
        e=e+1
    else:
        d=d+1
    c = input("enter c: ")
print(a)
print(b)
print(e)
print(d)