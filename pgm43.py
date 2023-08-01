# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:04:16 2023
single,double,three and four digit no or not using elif
@author: Dell
"""
a=int(input("Enter a"))
if a>=0 and a<=9:
    print("single digit")
elif a>=10 and a<=99:
    print("two digit")
elif a>=100 and a<=999:
    print("three digit")
elif a>=1000 and a<=9999:
    print("four digit")
else:
    print("not")
