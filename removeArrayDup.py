def removeDup(array):
    N = len(array)
    if N <= 1:
        return array

    temp = array[:1]
    for i in xrange(1, N):
        try:
            # print i, len(array), array[i]
            if array[i] != array[i - 1]:
                temp.append(array[i])
        except Exception as e:
            print e, i, len(array)

    return temp

# Allow 2 duplicates at max


def removeDup2(A):
    N = len(A)

    count = 1
    j = 0

    for i in xrange(1, N):

        if A[j] != A[i]:
            count = 0
            j += 1
            A[i], A[j] = A[j], A[i]
        elif A[j] == A[j] and count <= 1:
            j += 1
            A[i], A[j] = A[j], A[i]

        count += 1

    return A[:j + 1]


def removeDup_inplace(A):
    if len(A) <= 1:
        return A

    j = 0

    for i in xrange(1, len(A)):
        if A[j] != A[i]:
            j = j + 1
            A[i], A[j] = A[j], A[i]

    return A[:j + 1]


array = list([0, 1, 1, 2, 3, 3, 3, 4, 5])
print 'original:\n', array

print 'extra list:\n', removeDup(array)
print 'inplace:\n', removeDup_inplace(array)

array = list([0, 1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 5])
print '\nOriginal of 2 dups at most :\n', array
print removeDup2(array)
