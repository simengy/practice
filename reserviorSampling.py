import random


def reservior(streaming, N):
    sample = []
    for cnt, line in enumerate(streaming):
        if cnt < N:
            sample.append(line)
        else:
            if random.random() < N / float(i + 1):
                replace = random.randint(0, len(sample) - 1)
                sample[replace] = line
    return sample


data = [random.randint(0, 15) for i in xrange(10)]
print data
print reservior(data, 5)
