import numpy as np

def rotateImage(matrix):

    M = matrix.shape[0] # rnows
    N = matrix.shape[1] # cols
    rotateM = np.zeros((N, M))
    for i in range(M):
        
        for j in range(N):

            rotateM[j,N-i] = matrix[i, j]

    return rotateM

# in-place: square matrix
def rotateImage2(matrix):
    M = matrix.shape[0]
    N = matrix.shape[1]
    
    assert M == N
        
    for i in xrange(N):
        for j in xrange(N-i):
            swap(matrix, [i, j], [N-1-j, N-1-i])

    print 'debug\n', matrix

    for i in xrange(N/2):
        for j in xrange(N):
            swap(matrix, [i, j], [N-1-i, j])

    return matrix

def swap(matrix, pos1, pos2):
    
    temp = matrix[pos1[0]][pos1[1]]
    matrix[pos1[0]][pos1[1]] = matrix[pos2[0]][pos2[1]]
    matrix[pos2[0]][pos2[1]] = temp
    
    return None



matrix = np.array([[1,2],[3,4],[5,6]])
print matrix
print rotateImage(matrix)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print matrix
print rotateImage2(matrix)
