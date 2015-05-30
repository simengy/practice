def insertPos(array, target):
    
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) / 2

        if array[mid] > target:
            end = mid - 1
            
            if end < 0:
                return 0
            elif target > array[end] :
                return mid
        elif array[mid] == target:
            return mid
        else:
            start = mid + 1

            if start >= len(array):
                return start 
            elif target < array[start]:
                return mid

    return None

array = [1,2,5,6]

print insertPos(array, 5)

print insertPos(array, 7)

print insertPos(array, 0)



