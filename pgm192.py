# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:48:00 2023

@author: Dell
"""

s1 = input('enter s1:')
s2 =" "
d1=int(input('enter d1:'))
for i in range(len(s1)):
    u=ord(d1)
    if u>=97 and u<=122:
        d1=u-32
        x=chr(d1)
        s2=s2+x
    else:
        s2=s2+s1[i]
print(s2)