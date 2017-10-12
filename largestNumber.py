# Given a list of non negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# Note: The result may be very large, so you need to return a string
# instead of an integer.


def largestNum(lst):
    largest = None

    if len(lst) == 1:
        return lst[0]

    for i in xrange(len(lst)):

        temp = lst[i + 1:]
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
    def compare(a, b):
        if a + b > b + a:
            return 1
        else:
            return -1

    largest = sorted([str(x) for x in A], cmp=compare, reverse=True)
    return ''.join(largest)


lst = [3, 30, 9, 34, 5]

# lst = [3 , 11]
print largestNum(lst)
print largestNum2(lst)
