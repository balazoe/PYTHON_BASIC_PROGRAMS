# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:36:32 2023

@author: Dell
"""

s1=input('enter s1:')
s2=""
m=int(input('enter m:'))
for i in range(m,len(s1)):
    s2=s2+s1[i]
print(s2)