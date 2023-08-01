# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:46:32 2023
character of uni code lower to upper
@author: Dell
"""

d1=input("enter d1")
u=ord(d1)
if u>=97 and u<=122:
    d1=u-32
    x=chr(d1)
    print(x)
    
