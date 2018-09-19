# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:02:03 2018

@author: fatih.dereli
"""
import numpy as np

palindrome=[]

for i in range (1,10):
    for j in range (0,10):
        for k in range (0,10):
            palindrome.append(i*100001+j*10010+k*1100)
            
print(max(palindrome))

product=[]

for a in range (100,1000):
    for b in range (100,1000):
        product.append(a*b)

print(max(product))

print(max(np.intersect1d(palindrome,product)))