def route(start, end):

    print start, end
    if start[0] > end[0]:
        return 0
    elif start[0] == end[0]:
        if start[1] == end[1]:
            return 1
        elif start[1] != end[1]:
            return 0
    else:
        temp = [0, 0]
        temp[0] = start[0] + 1
        count = 0

        direction = [-1, 0, 1]
        for i in direction:
            temp[1] = start[1] + i
            count += route(temp, end)
            
            # iterated all directions
            if i == 1:
                return count


if __name__ == '__main__':
    start = [1,1]
    end = [6,5]

    print 'Number of routes:'
    print route(start, end)
