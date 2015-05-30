def setZeros(matrix):

    pos = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if matrix[i][j] == 0:
                temp = [i,j] 

                pos.append(temp)

    put(matrix, pos)


def put(matrix, pos):

    for i in pos:
        row = i[0]
        col = i[1]
        for c in range(len(matrix[row])): 
            matrix[row][c] = 0

        for r in range(len(matrix)):
            matrix[r][col] = 0


matrix = [[1,2,3,4],[2,3,0,5],[0,3,2,5],[1,1,1,1]]

for i in matrix:
    print i
setZeros(matrix)

for i in matrix:
    print i
