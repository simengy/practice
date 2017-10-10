import random


def weightedSampling(weights, array):
    rd = random.random()

    # To start from 0
    bins = [0, ]
    tmp = 0

    for w in weights:
        tmp += w
        bins.append(tmp)

    index = binary_search_index(bins, rd)

    return array[index]


def binary_search_index(bins, number):
    head = 0
    tail = len(bins)
    mid = None

    while tail - head > 1:
        mid = (head + tail) / 2

        if number < bins[mid]:
            tail = mid
        else:
            head = mid

    return head


weights = [0.1, 0.3, 0.6]
numbers = [1, 2, 3]

count = {}
for i in xrange(10000):
    number = weightedSampling(weights, numbers)

    if number in count:
        count[number] += 1
    else:
        count[number] = 1

for v in count.iteritems():
    print v
