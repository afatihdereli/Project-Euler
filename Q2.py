# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:19:43 2018

@author: fatih.dereli
"""

a=1
b=2
fib=[a,b]

while a+b<4000000:
    c=a+b
    fib.append(c)
    a=b
    b=c
 
even=[]

for i in range(0,len(fib)):
    if fib[i] % 2 ==0:
        even.append(fib[i])
        
print(sum(even))