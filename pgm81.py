# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:54:54 2023
Read and display the number other than 1000 is posi,nega or not
@author: Dell
"""
c=int(input("Enter c"))
while c!=1000:
    print(c)
    if c>0:
        print("positive")
    elif c<0:
        print("negative")
    else:
        print("zero")
    c=int(input("Enter c"))
print(c)
