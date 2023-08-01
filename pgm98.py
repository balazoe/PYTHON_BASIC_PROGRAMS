# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:55:26 2023
print the pattern
@author: Dell
"""

n=1
c=1
while c<=5:
    c1=1
    while c1<=n:
        print('*',end='')
        c1=c1+1
    c=c+1
    n=n+1
    print()
n1=5
c2=1
while c2<=5:
    c3=1
    while c3<=n:
        print('*',end='')
        c3=c3+1
    c2=c2+1
    n=n-1
    print()
    