# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:04:16 2023
single,double,three and four digit no or not using elif
@author: Dell
"""
a1=input("Enter a1")
if a1>='0' and a1<='9':
    print("Digit")
elif a1>='A' and a1<='Z':
    print("Upper case")
elif a1>='a' and a1<='z':
    print("Lower case")
elif a1>='@' and a1<='#':
    print("special character")
else:
    print("not")
