def setZeros(matrix):
    '''
    O(M+N) extra space
    '''

    M = len(matrix)
    N = len(matrix[0])

    rowZeros = set()
    colZeros = set()

    for i in range(M):
        for j in range(N):

            if matrix[i][j] == 0:
                rowZeros.add(i)
                colZeros.add(j)

    for i in rowZeros:
        for j in range(N):
            matrix[i][j] = 0

    for j in colZeros:
        for i in range(M):
            matrix[i][j] = 0


def setZeros_constantSpace(matrix):
    '''
    O(2) extra space: using the first row and col as the indicators
    '''
    firstrow = False
    firstcol = False

    M = len(matrix)
    N = len(matrix[0])

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                if i == 0:
                    firstrow = True
                if j == 0:
                    firstcol = True
                if i != 0 or j != 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

    print matrix

    for i in range(1, M):
        if matrix[i][0] == 0:
            for k in xrange(N):
                matrix[i][k] = 0

    for j in range(1, N):
        if matrix[0][j] == 0:
            for k in xrange(M):
                matrix[k][j] = 0

    if firstrow:
        for k in xrange(N):
            matrix[0][k] = 0

    if firstcol:
        for k in xrange(M):
            matrix[k][0] = 0


matrix = [[1, 2, 3, 4], [2, 3, 0, 5], [0, 3, 2, 5], [1, 1, 1, 1]]

print 'Raw matrix:'
for i in matrix:
    print i
setZeros(matrix)

print 'Set Zero matrix:'
for i in matrix:
    print i


matrix = [[1, 2, 3, 4], [2, 3, 0, 5], [0, 3, 2, 5], [1, 1, 1, 1]]

print 'Raw matrix:'
for i in matrix:
    print i
setZeros_constantSpace(matrix)

print 'Set Zero matrix:'
for i in matrix:
    print i
