# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:04:16 2023
Arithmetic,Realtional,Logical operator or Other operator using elif
@author: Dell
"""
a1=input("Enter a1")
if a1=='+' or a1=='-' or a1=='%' or a1=='//':
    print("Arithmetic operator")
elif a1=='>' or a1=='!=' or a1=='>=' or a1=='==':
    print("Relational operator")
elif a1=='and' or a1=='or' or a1=='not':
    print("Logical operator")
elif a1=='True' or a1=='False':
    print("other operator")
else:
    print("not")
