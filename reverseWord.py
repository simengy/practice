# recursive
def reverseCharacter(word):
    if len(word) == 1:
        return word

    head = word[0]

    new_word = reverseCharacter(word[1:]) + head

    return new_word

# in-place
def reverseCharacter_v2(word):
    n = len(word) - 1

    for i in xrange(len(word) / 2):
        tmp = word[i]
        word[i] = word[n - i]
        word[n - i] = tmp


def reverseWord(sentense):
    words = sentense.split()
    new_sentense = ''

    for i in reversed(range(len(words))):
        new_sentense = new_sentense + words[i] + ' '

    return new_sentense

# in-place
def reverseWord2(sentense):
    reverseCharacter_v2(sentense)

    start = 0
    end = 0
    try:
        prev = sentense[0]
    except:
        return None

    for p in xrange(1, len(sentense)):
        if sentense[p] == ' ' and prev != ' ':
            end = p
            reverseCharacter_v2(sentense[start:end])
        elif sentense[p] != ' ' and prev == ' ':
            start = p - 1


if __name__ == '__main__':
    sentense = 'PangTao'
    sentense = list(sentense)

    print reverseCharacter_v2(sentense)
    print ''.join(sentense)

    sentense = ' here we come   Big Data'
    print reverseWord(sentense)

    sentense = list(sentense)
    print reverseWord2(sentense)
    print ''.join(sentense)
