def removeEl(array, num):

    N = len(array)
    i = 0

    while i < N:

        try:
            if array[i] == num:
                if i != 0:
                    temp = array[:i]
                else:
                    temp = []
                
                temp.extend(array[i+1:])
                array = temp
                N -= 1
                i -= 1

            i += 1
        except:
            pass


    return array

# in-place
def removeEl2(array, target):

    N = len(array)
    i = 0
    
    while i < N:
        
        if array[i] == target:
            
            N = N - 1
            for pos in range(i, N):
                
                array[pos] = array[pos+1]
            
            i = i - 1

        i += 1

    return array, N

        



array = [1,2,3,4,1,5,6,1,2,7]

print array
print removeEl(array, 1)
print removeEl2(array, 1)
