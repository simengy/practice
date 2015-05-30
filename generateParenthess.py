def parentheses(n1, n2):

    lst = []

    if n1 == 0 and n2 == 1:
        return ')'
    
    print n1, n2
    if n1 < n2:
        if n1 != 0:
            temp = parentheses(n1-1, n2)
            for p in temp:
                lst.append('('+p)
        if n2 != 0:
            temp = parentheses(n1, n2-1)
            for p in temp:
                lst.append(')'+p)
    elif n1 == n2:
        if n1 != 0:
            temp = parentheses(n1-1, n2)
            for p in temp:
                lst.append('('+p)
    else:
        return None
    return lst


n = 2

print parentheses(n, n)

