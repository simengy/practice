import math
from datetime import datetime


def countPrime(n):
    start = datetime.now()    
    count = 1 # since 2 is a prime number
    for i in xrange(3, n):

        prime = True
        for num in xrange(2, int(math.sqrt(i))+1):

            if i%num == 0:
                prime = False
                break
        
        if prime == True:
            count += 1
    print 'trial takes: ', datetime.now() - start 
    return count


def sieveCount(n):

    start = datetime.now()    
    A = [True] * (n - 1)
    
    for i in xrange(int(math.sqrt(n))):

        if A[i] is True:
            j = i
            while j < n - 1 - i - 2:
                j += i + 2
                A[j] = False

    count = 0
    for i in xrange(len(A)):
        if A[i] == True:
            count += 1
            #print i+2

    print 'sieve takes: ', datetime.now() - start 
    return count

print countPrime(1000000)
print sieveCount(1000000)
