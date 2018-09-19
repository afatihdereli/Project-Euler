# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:25:52 2018

@author: fatih.dereli
"""
#Takes about 9 mins to solve (4:29)
prime=[2]

for i in range (3,1999999,2):
    print(i)
    div=0
    for j in range(0,len(prime)):
        if i%prime[j]>0:
            div=div+1
    if div==len(prime):
        prime.append(i)
    
                
print(sum(prime))