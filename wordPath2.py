# the matrix marks whether the elements visited or not
touch = []

def wordPath(maze, word, x, y, pos):
   
    if pos == 0:
        for i in xrange(len(maze)):
            found = False
            for j in xrange(len(maze[i])):
                if maze[i][j] == word[pos]:
                    found = True
                    x = i
                    y = j
                    touch[i][j] = True
                    break
            if found == True:
                break
            
    if pos == len(word)-1:
        return True

    for i in xrange(-1,2):
        for j in xrange(-1,2):
        
            if i == 0 and j == 0:
                continue
            
            x_next = x + i
            y_next = y + j
            
            try:
                if maze[x_next][y_next] == word[pos+1] and touch[x_next][y_next] == False:
                    touch[x_next][y_next] = True
                    
                    if wordPath(maze, word, x_next, y_next, pos + 1):
                        return True
                    else:
                        touch[x_next][y_next] = False
                        continue
            except:
                # Using out-of-bound exception to replace the boundary check
                pass


    return False


maze = ['abce', 'sfcs', 'adee']
for i in xrange(len(maze)):
    print maze[i]
    touch.append([False]*len(maze[i]))


word = 'abcced'
word = 'see'
word = 'abcb'
print word
print wordPath(maze, word, -1, -1, 0)

