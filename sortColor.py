# Sort an array with 0,1,2
# Example: [0,2,1,0,2,1] --> [0,0,1,1,2,2]


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

# in-place


def sortColor_v2(array):
    N = len(array)
    ind1 = 0
    ind2 = N - 1
    i = 0

    while i <= ind2:
        if array[i] == 0:
            array[ind1], array[i] = array[i], array[ind1]
            ind1 += 1
            i += 1
        elif array[i] == 2:
            array[ind2], array[i] = array[i], array[ind2]
            ind2 -= 1
        else:
            i += 1


array = [0, 1, 2, 1, 2, 1, 2, 0, 1, 1]


print array
print sortColor(array)

sortColor_v2(array)
print array
