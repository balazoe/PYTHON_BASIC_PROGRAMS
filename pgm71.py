# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:46:32 2023
character of uni code upper to lower
@author: Dell
"""

d1=input("enter d1")
u=ord(d1)
if u>=65 and u<=90:
    d1=u+32
    x=chr(d1)
    print(x)
    
