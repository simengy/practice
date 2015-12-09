def wordBreak(sentence, dictionary, head):
   
    if head == len(sentence):
        return True

    for i in range(head+1, len(sentence)+1):
        if sentence[head:i] in dictionary:
            return wordBreak(sentence, dictionary, i)
            
    return False


def wordBreak2(string, dictionary):

    if len(string) == 0:

        return True

    for i in xrange(1, len(string)+1):
        
        if string[:i] in dictionary:

            if wordBreak2(string[i:], dictionary):
                return True
            else:
                return False

    return False


if __name__ == "__main__":

    dictionary = ['syan', 'come', 'here', 'from']
    print wordBreak('syancomefrom', dictionary, 0)
    print wordBreak2('syancomefrom', dictionary)
