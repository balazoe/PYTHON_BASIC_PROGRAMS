# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:31:26 2023

@author: Dell
"""

c = input("enter c: ")
while c!='$':
    print(c)
    if c<='A' and c<='Z':
        print('upper')
    elif c<='a' and c<='z':
        print('lower')
    elif c<='0' and c<='9':
        print('digit')
    else:
        print('special character')
    c = input("enter c: ")
print(c)