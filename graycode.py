def graycode(n):

    codesets = allsub(n)

    map = {}
    for code in codesets:
        sum = 0
        for i in reversed(range(len(code))):
            sum = sum * 2 + int(code[i])

        map[code] = sum

    return map

def allsub(n):

    if n == 0:
        return None
    elif n == 1:
        return ['0', '1']
    
    string = []
    
    for key in allsub(n-1):
        string.append( '1' + key)
        string.append('0' + key)

    return string


print allsub(3)
print allsub(2)

dictionary = graycode(3)
for i in dictionary:
    print i, dictionary[i]

