def sortColor(arrary):
    
    N = len(arrary)
    A = [1] * N
    ind1 = 0
    ind2 = N - 1

    for i in array:
        if i == 0:
            A[ind1] = 0
            ind1 += 1
        elif i == 2:
            A[ind2] = 2
            ind2 -= 1
        
    return A


array = [0,1,2,1,2,1,2,0,1,1]


print array
print sortColor(array)
        
