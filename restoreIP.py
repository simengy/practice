from atoi import atoi

def restoreIP(string, n):

    if n==1:
        if validRange(string):
            return [string,]
        else:
            return [None,]
    
    lst = []
    for i in range(1,len(string)):
        
        res = restoreIP(string[i:], n-1)
        for val in res:
            temp = ''
            if val is not None and validRange(string[:i]):
                temp = string[:i] + '.' + val

                lst.append(temp)
        
    return lst

def validRange(string):
    
    #print 'valid', string
    if atoi(string) >= 0 and atoi(string) <= 255 and \
    (len(string) == 2 and string[0] != '0') or \
    (len(string) == 3 and string[0] != '0' and string[1] != '0') or \
    len(string) == 1:
        return True
    else:
        return False


string = '25525511135'
print restoreIP(string, 4)
            
