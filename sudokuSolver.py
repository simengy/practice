def solver(grid, row, col, indicator):

    if row == len(grid):
        return True

    for i in range(1, 10):
        
        if col < len(grid[row])-1:
            next_col = col + 1
            next_row = row
        else:
            next_col = 0
            next_row = row + 1          
            
        if indicator[row][col] == 0:
                grid[row][col] = i
        
        if checker(grid, row, col, i) == True:
           
            if solver(grid, next_row, next_col, indicator):
                return True
            else:
                #print row, col, next_row, next_col, i, grid[row][col],'debug'
                #for k in grid:
                #    print k
                
                if indicator[row][col] == 0:
                    grid[row][col] = 0
                continue # redundance but for debug purpose
        else:
            if indicator[row][col] == 0:
                grid[row][col] = 0
            continue

    return False


def checker(grid, row, col, num):

    assert num in range(1, 10)

    for i in range(len(grid[row])):
        if grid[row][i] == num and i != col:
            return False

    for i in range(len(grid)):
        if grid[i][col] == num and i != row:
            return False

    start_row = int(row / 3) * 3
    start_col = int(col / 3) * 3
    
    for i in xrange(start_row, start_row+3):
        for j in xrange(start_col, start_col+3):
            if i == row and j == col:
                continue
            if grid[i][j] == num:
                return False

    return True


sudoku = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9],
        ]


indicator = []
for i in sudoku:
    temp = []
    for j in i:
        if  j == 0:
            temp.append(0)
        else:
            temp.append(1)
    indicator.append(temp)


print checker(sudoku, 0,2,4)
print checker(sudoku, 0,2,5)
print checker(sudoku, 0,3,6)
print checker(sudoku, 0,3,7)


print 'solver results:'
solver(sudoku, 0, 0, indicator)
for i in sudoku:
    print i

print 'sanity check of indicator:'
for i in indicator:
    print i
