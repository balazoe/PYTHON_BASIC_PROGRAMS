# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:54:54 2023
print 1000 to 3000 say leap year or not
@author: Dell
"""

c=1000
while c<=3000:
    d1=c%4
    if d1==0:
        print("leap year")
    else:
        print("not")
    c=c+1
print(c)
