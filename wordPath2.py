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
                    print 'found:', i, j
                    break
            if found == True:
                break

    if pos == len(word):
        return True

    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False

    if touch[x][y] == True:
        return False

    if word[pos] != maze[x][y]:
        return False

    touch[x][y] = True

    for i in xrange(-1, 2):
        for j in xrange(-1, 2):

            if i == 0 and j == 0:
                continue

            x_next = x + i
            y_next = y + j

            if wordPath(maze, word, x_next, y_next, pos + 1):
                return True

    touch[x][y] = False
    return False


maze = ['abce', 'sfcs', 'adee']
for i in xrange(len(maze)):
    print maze[i]
    touch.append([False] * len(maze[i]))


word = 'abcced'
#word = 'bfb'
#word = 'abc'
print 'Target word:', word
print wordPath(maze, word, -1, -1, 0)
