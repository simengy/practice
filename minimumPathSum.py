def minSum(grid, startx, starty):

    sum = 0
    minsum = None
    count = 0
    N = len(grid) - 1
    M = len(grid[0]) - 1

    if startx == M and starty == N:

        return grid[startx][starty], 1

    direction={1:[1,0], 2:[0,1]}
    
    for key, value in direction.iteritems():
        
        if startx + value[0] <= N and starty + value[1] <= M:
            
            sum, innerCount = minSum(grid, startx+value[0], starty+value[1])
            if sum:
                sum += grid[startx][starty]
                count += innerCount

                if minsum is None or minsum > sum:
                    minsum = sum
                #return minsum
            else:
                continue

    return minsum, count

grid = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
]

grid = [[1,2],
        [5,6],
]

print minSum(grid, 0, 0)

