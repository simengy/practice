def wordLadder(word, last, dictionary, label):
    
    if search(word, last):
        return True
    
    N = len(dictionary)
    for tag in range(N):

        if label[tag] == 1:
            continue
        else:
            print tag, word, dictionary[tag]
            
            if search(word, dictionary[tag]):
                label[tag] = 1
                
                if wordLadder(dictionary[tag], last, dictionary, label):
                    return True
                else:
                    if tag == N - 1:
                        return False
                    else:
                        label[tag] = 0
                        continue
            else:
                continue

    return False

def search(word, tag):

    count = 0
    for i in range(len(word)):
        if word[i] == tag[i]:
            count += 1
    
    if count == len(word) - 1:
        return True
    else:
        return False


dictionary = ['hot', 'dot', 'dog', 'lot', 'log' ]
# indicator to represent whether the words have been touched or not
label = [ 0 for i in range(len(dictionary))]
word = 'hit'
last = 'cog'
print label
print wordLadder(word, last, dictionary, label)
