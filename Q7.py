# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:14:05 2018

@author: fatih.dereli
"""
#Takes about 9 mins to solve
prime=[]
i=2

while len(prime)<10001:
    #print(len(prime))
    div=0
    for j in range(1,i+1):
        if i%j==0:
            div=div+1
    if div==2:
        prime.append(i)
    i=i+1
                
print(max(prime))