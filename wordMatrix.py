def searchAround(matrix, i, j, startx, starty, letter):

    for deltaX in xrange(startx, 2):
        for deltaY in xrange(starty, 2):
            if deltaX == 0 and deltaY == 0:
                continue

            if i + deltaX >= 0 and i + deltaX < len(matrix) \
                    and j + deltaY >= 0 and j + deltaY < len(matrix[0]):
                if matrix[i + deltaX][j + deltaY] == letter:
                    return deltaX, deltaY
    return None, None


def findWord(matrix, x, y, word, pos):
    if pos >= len(word):
        return True

    startX = -1
    startY = -1
    while startX is not None:
        startX, startY = searchAround(matrix, x, y, startX, startY, word[pos])
        if startX is not None:
            x += startX
            y += startY
            if findWord(matrix, x, y, word, pos + 1):
                return True

    return False

wordM = ['worxb', 'helob', 'indem']
print findWord(wordM, 0, 0, 'wend', 1)
