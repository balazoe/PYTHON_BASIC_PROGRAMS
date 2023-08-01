# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:34:39 2023
draw the pattern
*****
****
***
**
*
**
***
****
*****
@author: Dell
"""

n=5
c=1
while c<=5:
    c1=1
    while c1<=n:
        print('*',end='')
        c1=c1+1
    c=c+1
    n=n-1
    print()
n=2
c2=1
while c2<=4:
    c3=1
    while c3<=n:
        print('*',end='')
        c3=c3+1
    c2=c2+1
    n=n+1
    print()
