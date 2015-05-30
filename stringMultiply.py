def strMultiply(num1, num2):

    num1 = num1[::-1]
    num2 = num2[::-1]
    res = [0 for i in xrange(len(num1)+len(num2))]
    
    for i in xrange(len(num1)):
        
        carry = 0
        for j in xrange(len(num2)):

            res[i+j] += carry + int(num1[i]) * int(num2[j])
            carry = res[i+j] / 10
            res[i+j] = res[i+j] % 10
        res[i+j+1] += carry 
    
    return res


num1 = '454'
num2 = '925'
print 'check', num1, num2
print strMultiply(num1, num2)
print int(num1) * int(num2)

