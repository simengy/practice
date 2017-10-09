# Allow duplicate element
def combinationSum(candidate, target):

    if len(candidate) == 1 and target != candidate[0]:
        return None
    if target < 0:
        return None

    candidate = sorted(candidate)
    sub = []

    for i in xrange(len(candidate)):

        if candidate[i] < target:
            temp = combinationSum(candidate[i:], target - candidate[i])
            if temp:
                for k in temp:
                    # print k
                    k.append(candidate[i])
                    sub.append(k)

        elif candidate[i] == target:
            sub.append([candidate[i], ])

    return sub

# Unique values


def combinationSum2(candidate, target):

    if len(candidate) == 1 and target != candidate[0]:
        return None
    if target < 0:
        return None

    candidate = sorted(candidate)
    sub = []
    for i in xrange(len(candidate)):
        # repeating elements only use once
        if i != 0 and candidate[i] == candidate[i - 1]:
            continue

        if candidate[i] < target:
            temp = combinationSum2(candidate[i + 1:], target - candidate[i])
            if temp:
                for k in temp:
                    # print k
                    k.append(candidate[i])
                    sub.append(k)

        elif candidate[i] == target:
            sub.append([candidate[i], ])

    return sub


candidate = [2, 3, 6, 7]
target = 7
print 'combinationSum 1:', combinationSum(candidate, target)

candidate = [10, 1, 2, 7, 6, 1, 5]
target = 8
print 'combinationSum 2:', combinationSum2(sorted(candidate), target)
