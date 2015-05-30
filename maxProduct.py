def maxProd(array):

    max = 0
    start = 0
    end = 0

    for i in xrange(len(array)-1):
        prod = array[i]
        for j in xrange(i+1, len(array)):
            prod *= array[j]

            if max < prod:
                max = prod
                start = i
                end = j

    return max, start, end


def maxProd2(array):

    start = 0
    end = 0
    max_prod = array[0]
    min_prod = array[0]
    max_all = array[0]
    for i in xrange(1, len(array)):
        
        max_prod_temp = max_prod
        min_prod_temp = min_prod
        
        if max_prod_temp * array[i] < min_prod_temp * array[i]:
            max_prod = min_prod_temp * array[i]
            start = i
        else:
            max_prod = max_prod_temp * array[i]
        
        if max_prod < array[i]: 
            max_prod = array[i]
            start = i

        if min_prod_temp * array[i] > max_prod_temp * array[i]:
            min_prod = max_prod_temp * array[i]
        else:
            min_prod = min_prod_temp * array[i]
        
        if min_prod > array[i]:
            min_prod = array[i]
        
        if max_all < max_prod:
            max_all = max_prod
            end = i

    return max_all, start, end


arr = [2,3,3,-2,-1,4,3,4,-2]
print maxProd(arr)
print maxProd2(arr)
