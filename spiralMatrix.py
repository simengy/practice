def spiral(n, mat, init, pos):

    if n == 0:
        return
    elif n == 1:
        mat[pos][pos] = init
        return

    N = len(mat)
    for i in range(n-1):
        
        mat[pos][pos+i] = init + i
        mat[N-1-pos][N-1-i-pos] = init + 2*n - 2 + i
        mat[N-1-i-pos][pos] = init + 3*n - 3 + i
        mat[i+pos][N-1-pos] = init + n - 1 + i

    spiral(n-2, mat, init+4*n-4, pos+1)
    return


if __name__ == '__main__':
    
    mat = []
    n = 5

    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
    
        mat.append(row)
    
spiral(n, mat, 1, 0)

for i in mat:
    print i
        

