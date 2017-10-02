import copy


def countAndSay(n):

    if n == 1:
        return '1'

    lst = ''
    sub = countAndSay(n - 1)
    print sub
    i = 0
    while i < len(sub):
        if sub[i] == '1':
            if i != len(sub) - 1:
                if sub[i + 1] == '1':
                    lst = lst + '2' + '1'
                    i += 1
                else:
                    lst = lst + '1' + '1'
            else:
                lst = lst + '1' + '1'
        elif sub[i] == '2':
            if i != len(sub) - 1:
                if sub[i + 1] == '2':
                    lst = lst + '2' + '2'
                    i += 1
                else:
                    lst = lst + '1' + '2'
            else:
                lst = lst + '1' + '2'
        i += 1
    return lst


def countAndSay_v2(n):
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
            last = ch

        count_str = copy.copy(newstr)

    return count_str


# print countAndSay(1)
# print countAndSay(2)
# print countAndSay(3)
# print countAndSay(6)
print countAndSay_v2(4)
