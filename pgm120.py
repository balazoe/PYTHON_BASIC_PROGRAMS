# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:00:50 2023

@author: Dell
"""

s1 = input('enter s1:')
s2 =" "
m=int(input('enter m:'))
i=m
while i<len(s1):
    s2=s2+s1[i]
    i=i+1 
print(s2)