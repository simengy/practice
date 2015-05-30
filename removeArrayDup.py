def remove(array):

    arrary = sorted(array)
    N = len(array)

    i = 1
    while i < N:
        try:
            print i, len(array), array[i]
            if array[i] == array[i-1]:

                temp = array[:i-1]
                temp.extend(array[i:])
                print temp
                array = temp[:]
                i = i-1
                N = N-1

            i = i + 1
        except:
            print i, len(array)

    
    return temp

# Allow 2 duplicates at max
def removeDup2(A):

    A = sorted(A)
    N = len(A)

    count = 1
    i = 0
    while i < N:
        
        if A[i] == A[i-1] and i != 1:
            count += 1
        else:
            count = 1

        if count > 2:
            print 'count', i, A[i], A[i+1]
            for j in xrange(i,N-1):
                A[j] = A[j+1]

            i -= 1
            N -= 1
        
        i += 1
    
    print A
    return N, A

    

array = list([0,1,1,2,3,3,3,4,5])

print remove(array)

array = list([0,1,1,2,3,3,3,4,4,4,4,5])

print 'again\n',array
N, temp = removeDup2(array)
for i in xrange(N):
    print temp[i]
