def reverseCharacter(word):

    if len(word) == 1:
        return word

    head = word[0]
 
    new_word = reverseWord(word[1:]) + head
    
    return new_word

def reverseWord(sentense):
    
    words = sentense.split()
    new_sentense = ''

    for i in reversed(range(len(words))):
        
        new_sentense = new_sentense + words[i] + ' '

    return new_sentense


if __name__ == '__main__':
    print reverseCharacter('PangTao')

    sentense = ' here we come   Big Data'

    print reverseWord(sentense)

