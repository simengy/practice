def distance(x1, x2, y1, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def distance_sum(ppl, centeroid):
    assert type(ppl) is list, 'check data type!'
    dis_sum = 0
    for p in ppl:
        dis_sum += distance(p[0], centeroid[0], p[1], centeroid[1])

    return dis_sum


def optimizer(width, length, ppl):
    centeroid = [0, 0]
    min_dis = None
    centeroid = None

    for i in xrange(width):
        for j in xrange(length):
        	curr_dis = distance_sum(ppl, [i, j])
        	if min_dis is None or min_dis > curr_dis:
        		min_dis = curr_dis
        		centeroid = [i, j]

    return min_dis, centeroid


if __name__ == '__main__':
	print optimizer(4, 4, [[0,0], [3,3], [1,2]])