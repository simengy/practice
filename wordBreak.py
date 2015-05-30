def wordbreak(string, dictionary, start):

    if len(string) == start:
        return True
    
    count = 0
    for i in string[start:]:
        
        print start, i
        count  = count + 1
        end = start + count

        temp = string[start:end]

        if temp in dictionary:
            return wordbreak(string, dictionary, end)
        elif len(string) == end:
            return False


def wordbreak2(string, dictionary):

    if len(string) == 0:

        return True

    for i in xrange(1, len(string)+1):
        
        if string[:i] in dictionary:

            if wordbreak2(string[i:], dictionary):
                return True
            else:
                return False

    return False


if __name__ == "__main__":

    dictionary = ['syan', 'come', 'here', 'from']
    print wordbreak('syancomfrom', dictionary, 0)
    print wordbreak2('syancomfrom', dictionary)
