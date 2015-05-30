def close3sum(array, total):

    array = sorted(array)

    first = 0
    second = 0
    third = 0
    close = None

    for i in xrange(len(array)):

        res = total - array[i]
        print res, total, array[i]

        head = 0
        tail = len(array) - 1

        while(head < tail):

            if head == i:
                head += 1
                continue
            if tail == i:
                tail -= 1
                continue
            
            twosum = array[head] + array[tail]
            
            #print close, second, third 
            if close > abs(res-twosum) or close is None:
                close = abs(res-twosum)
                first = i
                second = head
                third = tail
            elif close == 0:
                first = i
                second = head
                third = tail
                return first, second, third, close


            if twosum > res:
                tail -= 1
                if tail == i:
                    tail -= 1
            elif twosum < res:
                head += 1
                if head == i:
                    head += 1
            
            
    return first, second, third, close


array = [1,3,5,8,10,22]
print close3sum(array, 17)
