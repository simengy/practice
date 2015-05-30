def merge(arr1, arr2):

    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    ind1 = 0
    ind2 = 0
    arr = []
    while ind1 < len(arr1) or ind2 < len(arr2):
        
        if ind1 < len(arr1) and ind2 < len(arr2):
            if arr1[ind1] > arr2[ind2]:
                arr.append(arr2[ind2])
                ind2 += 1
            else:
                arr.append(arr1[ind1])
                ind1 += 1
        elif ind1 == len(arr1):
            arr.append(arr2[ind2])
            ind2 += 1
        else:
            arr.append(arr1[ind1])
            ind1 += 1
        
    return arr

arr1 = [2, 4, 5, 7]
arr2 = [3, 6, 9, 11]

print merge(arr1, arr2)

