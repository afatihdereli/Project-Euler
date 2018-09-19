# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
list3=[]
list5=[]

for x in range(1000):
    if x % 3 == 0:
        list3.append(x)
    else:
        if x % 5 == 0:
            list5.append(x)


print(sum(set(list3+list5)))