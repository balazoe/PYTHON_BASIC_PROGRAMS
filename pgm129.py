# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 17:52:58 2023

@author: Dell
"""

s1=input()
s2=""
n=int(input())
m=int(input())
i=m
while i<m+n:
    s2=s2+s1[-i]
    i=i+1
print(s2)