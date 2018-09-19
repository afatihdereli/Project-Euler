# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:35:28 2018

@author: fatih.dereli
"""
#Ki<j and j<k can be added
for i in range(1,1001):
    for j in range(1,1001):
        for k in range(1,1001):
            if i+j+k==1000:
                if pow(i,2)+pow(j,2)==pow(k,2):
                    print(i,j,k)
                    print(i*j*k)
