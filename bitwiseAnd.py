from datetime import datetime


def bitWiseAnd(m , n):

    result = m
    for i in range(m+1, n+1):
        result = operatorAnd(result, i)

    return result

def binary(x):
    
    s = ''

    while x > 0:

        s = s + str(x % 2)
        x = x / 2

    return s

def operatorAnd(a, b):

    a = binary(a) 
    b = binary(b)
   
    N = 0
    if len(a) > len(b):
        N = len(a)
    else:
        N = len(b)
    
    num = 0
    digit = 1
    for i in xrange(N):
        
        try:
            if a[i] == '1' and b[i] == '1':
                num += digit
        except:
            pass
        digit *= 2

    return num

def bitWiseAnd2(m, n):

    p = 0
    while m != n:
        m >>= 1
        n >>= 1
        p += 1

    return m << p

start = datetime.now()
print  bitWiseAnd(69998, 70000)
p1 = datetime.now()
print 'method1 takes time:', p1 - start

print  bitWiseAnd2(69998, 70000)
print 'method2 takes time:', datetime.now() - p1
