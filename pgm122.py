# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:11:49 2023

@author: Dell
"""

s1=input('ENTER STRING:')
s2=""
n=int(input("ENTER N:"))
n1=len(s1)
i=n1-n
while i<n1:
    s2=s2+s1[i]
    i=i+1
print(s2)