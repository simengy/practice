def minWindowSubstring(s, t):

    toFind = {}

    for i in t:

        if i not in toFind:
            toFind[i] = 1
        else:
            toFind[i] += 1

    head = 0
    tail = 0 
    minSub = s[:]
    found = {}

    while tail < len(s):
        
        tag = True

        if s[tail] not in found:
            found[s[tail]] = 1
        else:
            found[s[tail]] += 1

        if s[tail] in toFind:
            if found[s[tail]] >= toFind[s[tail]]:
                found[s[head]] -= 1
                head += 1

        # Check the match between substring and target string
        for key in toFind:
            try:
                if found[key] < toFind[key]:
                    tag = False
                    break
            except:
                print 'No key'
                tag = False
                break

        if tag == True and len(minSub) > tail - head + 1:
            minSub = s[head:tail+1]
            tail -= 1

        tail += 1

    return minSub

S = 'aabdeefkfsyanfgr'
T = 'fan'

print minWindowSubstring(S, T)
