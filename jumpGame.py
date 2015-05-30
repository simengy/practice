def jumpGame(grid, pos):

    N = len(grid)
    
    if pos >= N - 1:
        return True


    for steps in xrange(1, grid[pos]+1):

        if jumpGame(grid, pos+steps):
            return True
        else:
            continue


    return False


A = [2,0,0,1,4]
print jumpGame(A, 0)

A = [3,2,1,0,4]
print jumpGame(A, 0)
            
