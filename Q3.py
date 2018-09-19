# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:45:37 2018

@author: fatih.dereli
"""

a=600851475143 
prime=[]

#if a is not 1 100000 should be increased
for i in range (3,100000,2):
    if a%i==0:
        prime.append(i)
        a=a/i
        
print(max(prime))