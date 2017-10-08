# implementation of quicksort


def partition(array, low, high):

    pivot = array[high]
    pos = low - 1

    for i in xrange(low, high):
        if pivot > array[i]:
            pos += 1

            tmp = array[i]
            array[i] = array[pos]
            array[pos] = tmp

    tmp = array[pos + 1]
    array[pos + 1] = array[high]
    array[high] = tmp

    return pos + 1


def quicksort(array, low, high):

    if len(array) <= 1:
        return

    if low < high:
        pivot = partition(array, low, high)

        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)


a = [12, 3, 6, 1, 14, 9, 7]

quicksort(a, 0, len(a) - 1)

print a
