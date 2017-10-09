def lookup(letter, maze, row, col, delta_row, delta_col):

    for i in range(delta_row, 2):
        for j in range(delta_col, 2):

            if i == 0 and j == 0:
                continue
            else:
                if row + i < 0 or row + i >= len(maze):
                    continue
                elif col + j < 0 or col + j >= len(maze[row]):
                    continue

            if letter == maze[row + i][col + j]:
                return row + i, col + j

    return None, None


def path(word, maze, pos, row, col):

    if pos == len(word) - 1:
        return True

    delta_row = -1
    delta_col = -1

    while(1):

        next_row, next_col = lookup(
            word[pos + 1], maze, row, col, delta_row, delta_col)
        # print next_row, next_col, row, col, delta_row, delta_col, word[pos +
        # 1]

        if next_row is not None:
            if path(word, maze, pos + 1, next_row, next_col):
                return True
            else:
                delta_row = next_row - row
                delta_col = next_col - col

                if delta_col == 1:
                    delta_row = delta_row + 1
                    delta_col = -1
                else:
                    delta_col = delta_col + 1

        else:
            return False


def shortest_path(word, maze, pos, row, col):
    step = None
    if pos >= len(word) - 1:
        return 1

    delta_row = -1
    delta_col = -1

    while(1):
        next_row, next_col = lookup(
            word[pos + 1], maze, row, col, delta_row, delta_col)
        # print step, pos, next_row, next_col, row, col, delta_row, delta_col,
        # word[pos + 1]
        if next_row is None:
            return step
        tmp = shortest_path(word, maze, pos + 1, next_row, next_col)
        if tmp:
            tmp += 1
            if step is None or tmp < step:
                step = tmp

        delta_row = next_row - row
        delta_col = next_col - col
        if delta_col == 1:
            delta_row = delta_row + 1
            delta_col = -1
        else:
            delta_col = delta_col + 1


if __name__ == '__main__':

    maze = ['worlb', 'helov', 'indem']

    for i in maze:
        print i

    print 'Any Path:', path('whnd', maze, 0, 0, 0)
    print 'Shortest Path:', shortest_path('world', maze, 0, 0, 0)
