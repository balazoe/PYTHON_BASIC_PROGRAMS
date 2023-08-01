# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:56:37 2023

@author: Dell
"""

import random
n=int(input('enter n:'))
a=[random.randint(-100,100) for i in range(n)]
b=[i for i in a if i>0]
print(a)
print(b)