# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:25:50 2023

@author: Dell
"""

s1=input()
s2=""
n=int(input())
m=int(input())
for i in range(-m,-m-n,-1):
    s2=s2+s1[i]
print(s2)