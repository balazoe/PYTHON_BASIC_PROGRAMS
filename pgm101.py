# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:33:49 2023
draw the pattern
@author: Dell
"""

n=0
n1=5
c=1
while c<=5:
    c1=1
    while c1<=n:
        print('-',end='')
        c1=c1+1
    c2=1 
    while c2<=n1:
        print('*',end='')
        c2=c2+1
    c=c+1
    n=n+1
    n1=n1-1
    print()