def letterCombination(number, mapping):
    
    if len(number) == 1:

        return mapping[number[0]]
    
    lst = []

    for i in mapping[number[0]]:
        for j in letterCombination(number[1:], mapping):
            print j 
            lst.append(i + j)

    return lst

mapping = {}
mapping['1'] = []
mapping['2'] = 'abc'
mapping['3'] = 'def'
mapping['4'] = 'ghi'


print letterCombination('23', mapping)

