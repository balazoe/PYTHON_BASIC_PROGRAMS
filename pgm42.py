# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:04:16 2023
single,double,three and four digit no or not
@author: Dell
"""
a=int(input("Enter a"))
if a>=0 and a<=9:
    print("single digit")
else:
    if a>=10 and a<=99:
        print("two digit")
    else:
        if a>=100 and a<=999:
            print("three digit")
        else:
            if a>=1000 and a<=9999:
                print("four digit")
            else:
                print("not")