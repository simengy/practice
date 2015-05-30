def countAndSay(n):

    if n == 1:
        return '1'
    
    lst = ''
    sub = countAndSay(n-1)
    print sub
    i = 0
    while i < len(sub):
        if sub[i] == '1':
            if i != len(sub) - 1:
                if sub[i+1] == '1':
                    lst = lst + '2' + '1'
                    i += 1
                else:
                    lst = lst + '1' + '1'
            else:
                lst = lst + '1' + '1'
        elif sub[i] == '2':
            if i != len(sub) - 1:
                if sub[i+1] == '2':
                    lst = lst + '2' + '2'
                    i += 1
                else:
                    lst = lst + '1' + '2'
            else:
                lst = lst + '1' + '2'
        i += 1
    return lst


#print countAndSay(1)
#print countAndSay(2)
#print countAndSay(3)
print countAndSay(4)

    
