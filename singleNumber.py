def singleNumber(array):

    count = {}
    for i in array:

        if str(i) not in count:
            count[str(i)] = 1
        else:
            count[str(i)] += 1
        
    return count



array = [2,2,3,3,7,14,7,8,9,8,9]

A = singleNumber(array)
for key in sorted(A, key=A.get, reverse=True):
    print key, A[key] 

