# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:54:54 2023
print the number even or odd
@author: Dell
"""
a=int(input("Enter a"))
b=int(input("Enter b"))
c=a
while c<=b:
    d1=c%2
    if d1==0:
        print("even")
    else:
        print("not")
    c=c+1
print(c)
