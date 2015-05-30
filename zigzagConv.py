def zigZag(s, nrows):

    # even rows K letters, and odd rows 2*K-1
    N = len(s)
    lst = []
    temp = []
    i = 0
    while i<N:
        
        if len(lst) % 2 == 0:
            temp.append(s[i])
        else:
            if len(temp) % 2 == 0:
                temp.append(' ')
                i -= 1
            else:
                temp.append(s[i])
        
        if len(temp) == nrows:
            lst.append(temp)
            temp = []

        i += 1

    for i in lst:
        print i
    
    new_s = ''
    for i in xrange(len(lst[0])):
        for j in xrange(len(lst)):
            
            try:
                if lst[j][i] != ' ':
                    new_s = new_s + lst[j][i]
            except:
                print j, i, ' No Element'
                pass

    return new_s

s = 'abcdefghjik'

new_s = zigZag(s, 3)
print 'new:'
print new_s
