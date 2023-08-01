# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:02:04 2023

@author: Dell
"""

s1 = input('enter s1:')
s2 =" "
d1=int(input('enter d1:'))
i=0
while i<len(s1):
    u=ord(d1)
    if u>=65 and u<=90:
        d1=u+32
        x=chr(d1)
        s2=s2+x
    else:
        s2=s2+s1[i]
        i=i+1
print(s2)