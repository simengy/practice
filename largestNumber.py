def largestNum(lst):

    largest = None

    if len(lst) == 1:

        return lst[0]

    for i in xrange(len(lst)):
         
        temp = lst[i+1:]
        temp.extend(lst[:i])
        comp = largestNum(temp)
        comp = lst[i] * (10 ** len(str(comp))) + comp
        
        if largest:
            if largest < comp:
                largest = comp
        else:
            largest = comp

    return largest


def largestNum2(A):

    prev = A[0]
    for i in xrange(1, len(A)):

        num1 = prev * 10 ** len(str(A[i])) + A[i]
        num2 = A[i] * 10 ** len(str(prev)) + prev
        
        # Overflow ?
        if num1 > num2:
            prev = num1
        else:
            prev = num2

    return prev




lst = [3, 30, 34, 5, 9]

#lst = [3 , 11]
print largestNum(lst)
print largestNum2(lst)
