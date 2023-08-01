# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:57:13 2023

@author: Dell
"""

a = 1
for i in range(4,0,-1):
    print(' ' * i + '*' * a)
    a = a + 2
a1 = 5
for a2 in range(2, 5):
    print(' ' * a2 + '*' * a1)
    a1 = a1 - 2