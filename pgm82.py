# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:54:54 2023
count the number other than 1000 is posi,nega or not
@author: Dell
"""
a=b=d=0
c=int(input("Enter c"))
while c!=1000:
    print(c)
    if c>0:
        a=a+1
    elif c<0:
        b=b+1
    else:
        d=d+1
    c=int(input("Enter c"))
print(a)
print(b)
print(d)
print(c)
