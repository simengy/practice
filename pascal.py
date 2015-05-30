def pascal(n):

    a = [1]

    for i in range(0, n):
        
        a.append(0)
        
        for c in reversed(range(1, len(a))):
            
            a[c] = a[c] + a[c-1]
        
        print a

pascal(5)

