# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:15:06 2023

@author: Dell
"""

b=0
c=1
while c<=10:
    a=int(input('enter a: '))
    if a<b:
        b=0
    else:
        print('not')
    c=c+1
print(b)
    