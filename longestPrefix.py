def longestPrefix(string):

    prefix = []
    same = True
    for i in xrange(len(string[0])):

        first = None
        try:
            for j in string:
                if first:
                    if j[i] != first:
                        same = False
                        break
                else:
                    first = j[i]

            if same == True:
                prefix.append(j[i])
        except:
            break


    return prefix

string = ['abcd',
        'abcdef',
        'abcde',
        'abcdffff'
        ]


print longestPrefix(string)

        

