# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:04:23 2023
Biggest as well as Smallest of 10 numbers
@author: Dell
""" 
b=20
c=1 
while c<=10:
    a=int(input("Enter a"))
    e=int(input("Enter e"))
    if a>b:
        b=a
    elif a<e:
        e=a
    else:
        print("not")
    c=c+1
print(b)
print(e)