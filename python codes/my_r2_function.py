# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 20:47:36 2018

@author: hp
"""
import numpy as np

def my_r2_function(predicted,real):
    A=predicted
    B=real
    M=np.mean(B)
    C=B-A
    K=B-M
#    for i in range(k):
 #       C[i]=A[i]-B[i]
    S=np.square(C)
    L=np.square(K)
    H=np.sum(S)
    U=np.sum(L)
    my_r2=1-(H/U)
    return(my_r2)  