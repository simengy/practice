import copy


def countAndSay(n):
    if n == 1:
        return '1'

    count_str = '1'

    for i in xrange(2, n + 1):
        count = 1
        last = None
        newstr = ''
        for pos in xrange(len(count_str) + 1):
            if pos == len(count_str):
                ch = '\0'
            else:
                ch = count_str[pos]

            if last != ch and last:
                newstr += str(count)
                newstr += last
                count = 1
            elif last == ch:
                count += 1
            # else: do nothing

            last = ch

        count_str = copy.copy(newstr)

    return count_str


for i in xrange(1, 8):
    print countAndSay(i)
