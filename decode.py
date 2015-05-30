def decode(code):

    map = {}
    for i in range(26):
        key = str(i+1)
        map[key] = chr(ord('a') + i)

    words = []
    c1 = subset(code)
    
    for c in c1:
        lst = c.split('.')
        temp = ''
        for t in lst:
            if t in map:
                temp = temp + map[t]
            elif t == '':
                continue
            else:
                temp = None
                break
        
        if temp is not None:    
            words.append(temp)

    return words


def subset(code):
    
    if len(code) == 0 or len(code) == 1:
        return [code,]

    sub = []
    for i in range(1,len(code)+1): 

        interaction = ''

        for j in subset(code[i:]):
            
            interaction = code[:i] + '.' + j

            sub.append(interaction)

    return sub


code = 1234
code = str(code)
print subset(code)
print decode(code)
