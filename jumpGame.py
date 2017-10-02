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


def jumpGame2(grid, pos):
    minJump = None

    if pos >= len(grid):
        return 1

    for step in xrange(1, grid[pos]+1):
        tmp = jumpGame2(grid, pos+step) 
        if tmp:
            tmp += 1
            if minJump is None or tmp < minJump:
                minJump = tmp
        else:
            continue

    return minJump



A = [2,0,0,1,4]
print jumpGame(A, 0)
print jumpGame2(A, 0)

A = [1,2,1,2,4]
print jumpGame(A, 0)
print jumpGame2(A, 0)
            
