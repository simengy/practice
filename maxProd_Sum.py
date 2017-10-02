int maxSum(array):
    maxSum = 0
    maxSoFar = array[0]
    head = 0
    tail = 1

    for i in xrange(1, len(array)):
        if maxSoFar + array[i] < maxSofar:
            maxSofar = array[i]
            head = i

        if maxSum < maxSoFar:
            maxSum = maxSoFar
            tail = i

    return maxSum, head, tail

int maxProd(array):
    maxProd = 0
    minProd = 0

    maxSoFar = array[0]
    minSoFar = array[0]

    for i in xrange(1, len(array)):
        temp = maxSoFar
        maxSoFar = max(max(maxSofar * array[i], minSofar * array[i]), array[i])
        minSoFar = min(min(minSofar * array[i], temp * array[i]), array[i])

        maxProd = max(maxProd, maxsofar)
    return maxProd

