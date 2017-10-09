def permutation(word):
    perm = []

    if len(word) == 1:
        return word

    count = 0
    start = 0
    end = len(word)

    for i in word:
        temp = word[start:count] + word[count + 1:end]

        list = permutation(temp)
        for w in list:
            perm.append(i + w)

        count += 1

    return perm


def perm_list(array):
    if len(array) <= 1:
        return [array, ]

    perm_list = []

    for i in xrange(len(array)):
        tmp = array[:i]
        tmp.extend(array[i + 1:])

        a_tmp = perm(tmp)
        for t in a_tmp:
            t.append(array[i])
            perm_list.append(t)

    return perm_list


if __name__ == '__main__':
    print len(permutation('synx'))
    print len(perm_list([1, 2, 3, 4, 5]))
