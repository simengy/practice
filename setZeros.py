def setZeros(matrix):

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


matrix = [[1, 2, 3, 4], [2, 3, 0, 5], [0, 3, 2, 5], [1, 1, 1, 1]]

print 'Raw matrix:'
for i in matrix:
    print i
setZeros(matrix)

print 'Set Zero matrix:'
for i in matrix:
    print i
