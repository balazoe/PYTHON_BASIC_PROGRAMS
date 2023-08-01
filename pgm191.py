# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 19:21:55 2023

@author: Dell
"""

s1 = input('enter s1:')
s2=""
for i in range(len(s1)):
    u = ord(d1)
    if u >= 65 and u <= 90:
        d1 = u + 32
        x = chr(d1)
        s2 = s2 + x
    else:
        s2 += s1[i]
print(s2)

