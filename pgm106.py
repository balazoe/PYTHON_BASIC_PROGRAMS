# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 19:43:50 2023

@author: Dell
"""

n=3
n1=1
c=1
while c<=4:
    c1=1
    while c1<=n:
        print(' ',end='')
        c1=c1+1
    c2=1 
    while c2<=n1:
        print('*',end='')
        c2=c2+1
    c=c+1
    n=n-1
    n1=n1+2
    print()
n=1
n1=5
c=1
while c<=3:
    c1=1
    while c1<=n:
        print(' ',end='')
        c1=c1+1
    c2=1
    while c2<=n1:
        print('*',end='')
        c2=c2+1
    c=c+1
    n=n+1
    n1=n1-2
    print()