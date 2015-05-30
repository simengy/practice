def intToRoman(number):

    numeral = {1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'}
   
    arr = []
    dis = 1
    while number > 0:
        
        digit = number % 10

        digit *= dis

        arr.append(digit)
        
        number /= 10
        dis *= 10
    
    print arr, len(arr)
    roman = ''
    # pos=0 -- 1
    # pos=2 -- 10
    # pos=3 -- 100
    # pos=4 -- 1000
    one = 1
    for i in xrange(len(arr)):
       
        if arr[i] in numeral:
            roman += numeral[arr[i]] 
        else:
            five = 5 * one
            ten = 10 * one
            
            if arr[i] / one <= 3:
                for t in xrange(arr[i]/one):
                    roman += numeral[one]
            elif arr[i] / one == 4:
                roman += numeral[five]
                roman += numeral[one]
            elif arr[i] / one > 4 and arr[i]/ one < 9:
                roman += numeral[five]
                for t in xrange(arr[i]/one - 5):
                    roman += numeral[one]
            else:
                roman += numeral[ten]
                roman += numeral[one]
            
        one *= 10

    return roman[::-1]


print intToRoman(1954)
print intToRoman(1990)
print intToRoman(2014)
            

