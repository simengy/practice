from combination import combination

# Only combination
def subset(string):

    sub = []
    for i in range(1, len(string)+1):

        sub.append(combination(string, i))

    return sub

# There are duplicate in the string
def subset2(string):

    sub = []
    string = sorted(string)

    for i in range(1, len(string)+1):

        sub.append(combination2(string, i))

    return sub

def combination2(string, n):

    sub = []
    prev = None
    
    if n == 1:

        for i in string:

            if i != prev:
                sub.append(i)
            else:
                continue

            prev = i

        return sub

    for i in xrange(len(string)):
        
        if string[i] == prev:
            continue

        for k in combination2(string[i+1:], n-1):
            sub.append(string[i] + k)
        
        prev = string[i]

    return sub


if __name__ == '__main__':

    
    print subset('abcs')
    
    print subset2('abbs')
    print subset2('aaa')
    print combination2('aaaa', 1)
