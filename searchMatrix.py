# binary search of number in 2D sorted array
def search(matrix, target):

    row = 0
    col = 0

    M = len(matrix)
    N = len(matrix[0])
    start = 0
    end = M - 1

    while start <= end:
        print 'first loop', start, end
        ind = (start + end) / 2
        if target == matrix[ind][0]:
            return ind, 0

        if target > matrix[ind][0]:
            start = ind + 1
        else:
            end = ind - 1
        
    row = start - 1
    start = 0
    end = N - 1
    while start <= end:

        print 'second loop', start, end, row
        ind = (start + end) / 2
        if target == matrix[row][ind]:
            return row, ind

        if target > matrix[row][ind]:
            start = ind + 1
        else:
            end = ind - 1
    
    return None, None

matrix = [[1,2,3],[4,5,6],[7,8,9],[13,14,18]]

print search(matrix, 18)
