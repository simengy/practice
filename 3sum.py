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
                tail == tail - 1
                continue

            if vec[head] + vec[tail] > pivot:
                tail -= 1
            elif  vec[head] + vec[tail] < pivot:
                head += 1
            else:
                return i, head, tail, pivot

    return None, None, None

vec = [12,23,6,3,4,5,6,7,8]

print three_sum(vec, 33)


