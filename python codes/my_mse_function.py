###output is accuracy
import numpy as np

def my_mse_function(predicted,real):
    A=predicted
    B=real
    k=len(B)
    C=A-B
#    for i in range(k):
 #       C[i]=A[i]-B[i]
    S=np.square(C)
    H=np.sum(S)
    my_mse=H/k
    return(my_mse)   