# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:09:41 2018

@author: fatih.dereli
"""
powersum=0
sumpower=0
lim=100+1


for i in range(1,lim):
    powersum=powersum+pow(i,2)
    
for i in range(1,lim):
    sumpower=sumpower+i
    
sumpower=pow(sumpower,2)

print(sumpower-powersum)