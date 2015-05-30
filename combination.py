def combination(word, n):

    subset = []

    if len(word) == 0:
        return word
    elif n == 1:

        for i in word:
            subset.append(i)
        return subset


    for i in range(len(word)):

        temp = combination(word[i+1:], n-1)

        for s in temp:
            subset.append(word[i] + s)

    return subset


if __name__ == '__main__':

    print combination('love', 2)
