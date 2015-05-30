
def atoi(number):

    numberlist = []
    for i in range(10):
        numberlist.append(str(i))

    sum = 0
    for i in xrange(len(number)):
        
        if number[i] not in numberlist:
            return None

        # out of range?
        if sum * 10 / 10 == sum:
            sum = sum * 10 +  ord(number[i]) - ord('0')
        else:
            print 'out of range'
            return None

    return sum


'''
number1 = '12345'
number2 = '1B345'
number3 = '1234235923123820349583045723498573294545699999934645645345'

print atoi(number1, numberlist)
print atoi(number2, numberlist)
print atoi(number3, numberlist)
'''
