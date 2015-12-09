
# O(N^2) complexity
def maxSubArray(array):
    start = 0
    end = start
    max = 0
    
    for i in xrange(len(array)):
        for j in xrange(i+1, len(array)+1):
            
            temp = add(array[i:j])
            
            if max < temp:
                max = temp
                start = i
                end = j - 1
    
    return max, start, end

# O(N)
def maxSubArray_2(array):
    maxend = array[0]
    maxsub = array[0]
    start = 0
    end = 0

    for i in range(1, len(array)):
        
        if maxsub + array[i] < array[i]:
            maxsub = array[i]
            start = i
        else:
            maxsub = maxsub + array[i]

        if maxend < maxsub:
            maxend = maxsub
            end = i
    
    return maxend, start, end


def add(arr):
    sum = 0
    for i in arr:
        sum += i

    return sum


if __name__ == '__main__':
    
    array = [1,3,-5,5,3,-4,-2,1,2]
    print maxSubArray(array)
    print maxSubArray_2(array)

