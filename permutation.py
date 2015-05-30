def permutation(word):

    perm = []

    if len(word) == 1:
        return word

    count = 0
    start = 0
    end = len(word)
    
    for i in word:
    
        temp = word[start:count] + word[count+1:end]
        
        list = permutation(temp)
        for w in list:
            
            perm.append(i + w)
        
        count += 1

    return perm


if __name__ == '__main__':
    print permutation('synting')


