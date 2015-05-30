N = 1000000

def sqrt(y):
    
    if y < 0:
        print 'Y is negative number!'
        return None
    elif y == 0:
        return 0
    
    x_p = 2.
    x = 0.
    while x - x_p > 1E-5 or x_p - x > 1E-5:
        
        x = x_p
        x_p = x - (x * x - y) / (2 * x)

    return x_p
        

def pow(x, n):

    if x > N:
        print 'overflow!'
        return None
    elif n == 1:
        return x
    else:
        if n % 2 == 0:
            return pow(x, n/2) * pow(x, n/2)
        else:
            return x * pow(x, n/2) * pow(x, n/2)


print sqrt(2)
print pow(2, 5)
