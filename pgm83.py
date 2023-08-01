# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:54:54 2023
sum the number other than 1000 is posi,nega or not
@author: Dell
"""
a=b=0
c=int(input("Enter c"))
while c!=1000:
    print(c)
    if c>0:
        a=a+c
    elif c<0:
        b=b+c
    else:
        print("not")
    c=int(input("Enter c"))
print(a)
print(b)
print(c)
