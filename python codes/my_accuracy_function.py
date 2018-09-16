def my_accuracy_function(predicted,real):
    A=predicted
    B=real
    k=len(B)
    j=0
    for i in range(k):
        if A[i]==B[i]:
            j+=1
    my_accuracy=j/k
    percent=my_accuracy*100
    return(percent)
    

        
    