# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 14:20:26 2023
Reverse the digit
@author: Dell
"""
a=int(input("Enter a"))
d1=a%10
d2=a//10
d3=d2%10
d4=d2//10
d5=d1*100
d6=d3*10
d7=d4*1
d8=(d5+d6+d7)
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)
print(d7)
print(d8)