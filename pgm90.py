# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:18:19 2023

@author: Dell
"""

a=99
c=1
while c<=10:
    b=int(input('enter a: '))
    if a<b:
        a=b
    else:
        print('not')
    c=c+1
print(a)