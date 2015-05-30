def plusOne(array):

    one = 1
    for i in reversed(range(len(array))):
        print array[i]
        if array[i] == 9 and one == 1:
            array[i] = 0
            one = 1 
        else:
            array[i] += one
            one = 0

    return array, one

array = [1,2,3]
print plusOne(array)
array = [2,9,9]
print plusOne(array)
