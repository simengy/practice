def three_sum(vec, total):

    vec = sorted(vec)

    print vec

    for i in range(len(vec)):

        pivot = total - vec[i]
        head = 0
        tail = len(vec) - 1

        while head < tail:
            if head == i:
                head = head + 1
                continue
            elif tail == i:
                tail = tail - 1
                continue

            if vec[head] + vec[tail] > pivot:
                tail -= 1
            elif vec[head] + vec[tail] < pivot:
                head += 1
            else:
                return i, head, tail

    return None, None, None


def closest_three_sum(vec, total):

    vec = sorted(vec)
    print vec

    min_diff = None

    for i in range(len(vec)):
        pivot = total - vec[i]
        head = 0
        tail = len(vec) - 1

        while head < tail:
            if head == i:
                head = head + 1
                continue
            elif tail == i:
                tail = tail - 1
                continue

            diff = total - pivot - vec[head] - vec[tail]
            if diff > min_diff or min_diff is None:
                min_diff = diff
                min_head = head
                min_tail = tail
                min_3rd = i

            if vec[head] + vec[tail] > pivot:
                tail -= 1
            elif vec[head] + vec[tail] < pivot:
                head += 1
            else:
                return i, head, tail

    return min_head, min_tail, min_3rd

vec = [12, 23, 3, 4, 6, 8]

print three_sum(vec, 33)
print closest_three_sum(vec, 40)
