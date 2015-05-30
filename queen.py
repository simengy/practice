def queen(board, row):

    if row == len(board):
        
        return True

    N = len(board[row])
    
    print row, N

    for col in xrange(N):
        
        if checker(board, row, col):
            
            board[row][col] = 'Q'
            
            if queen(board, row+1):
                return True
            else:
                board[row][col] = 'o'

    return False
    

def checker(board, row, col):

    N = len(board)

    # 8 directions

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            
            if i == 0 and j == 0:
                continue
            
            r = row
            c = col
            
            while 1:        
                r += i
                c += j
            
                if r < 0 or r == N or c < 0 or c == N: 
                    break

                if board[r][c] == 'Q':
                    return False
    
    return True


if __name__ == '__main__':
    
    board = []
    n=8

    for i in xrange(n):
        
        row = []
        
        for j in xrange(n):

            row.append('o')

        board.append(row)

    print queen(board, 0)
    
    for i in board:
        print i
