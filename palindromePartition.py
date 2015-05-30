
def palindrome(string):

    new = string[::-1] 

    return new == string

def partition(string):

    if len(string) == 1 or len(string) == 0:
        return [string,]
    
    subset = []
    
    for j in xrange(1,len(string)+1):

        if palindrome(string[:j]) == False:
            continue
         
        for i in partition(string[j:]):
            temp = []
            temp.append(string[:j])
            temp.extend(i)    
        
            subset.append(temp)
    
    return subset

# min-cut
def partition2(string):

    if len(string) == 1 or len(string) == 0:
        return [string,]
    
    mincut = string[:] 
    for j in xrange(1,len(string)+1):

        if palindrome(string[:j]) == False:
            continue
         
        temp = []
        temp.append(string[:j])
        temp.extend(partition2(string[j:]))
        
        if len(mincut) > len(temp):
                mincut = temp    
        
    return mincut


if __name__ == '__main__':

    string = 'abcbd'

    print partition(string)
    print partition2(string)
