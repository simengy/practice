def bitsum(a1, a2):

    a = ''

    if len(a1) > len(a2):
        N = len(a1) + 1
        a1 = '0' + a1
        for i in range(len(a1)-len(a2)):
            a2 = '0' + a2
    else:
        N = len(a2) + 1
        a2 = '0' + a2
        for i in range(len(a2)-len(a1)):
            a1 = '0' + a1

    for i in range(N):
        a = '0' + a
    
    print a1
    print a2
    a = list(a)
    for i in reversed(range(N)):
        print N, a
        if a1[i] == '0' and  a2[i] == '0':
            a[i] = a[i]
        elif a1[i] !=  a2[i]:
            if a[i] == '0':
                a[i] = '1'
            else:
                a[i] = '0'
                a[i-1] = '1'
        else:
            a[i-1] = '1'

    return ''.join(a)

a1 = '1110'
a2 = '01011'

print bitsum(a1, a2)
