def anagram(words):

    sets = []
    for i in xrange(len(words)):
        temp = None
        
        if touched[i] == 1:
                continue

        touched[i] = 1

        for j in xrange(i+1, len(words)):
            
            if sorted(words[i]) == sorted(words[j]):
                if temp is None:
                    temp = []
                    temp.append(words[i])
                temp.append(words[j])
                touched[j] = 1

        if temp:
            sets.append(temp)

    return sets

def anagram2(words):
    
    lst = {}
    for i in words:
        temp = ''.join(sorted(i))
        
        if temp not in lst:
            lst[temp] = [i,]
        else:
            lst[temp].append(i)
    
    return lst


words = ['abc', 'acb', 'bbb', 'bcb', 'bca', 'cbb']
touched = [0 for i in range(len(words))]

print anagram(words)

lst = anagram2(words)
for key in lst:
    print key, lst[key]
