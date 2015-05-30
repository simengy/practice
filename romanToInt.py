def romanToInt(string):
    
    dictionary = {'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }

    prev = None
    number = 0
    for i in string:
        curr = dictionary[i]
        if prev:
            if curr > prev:
                number += -2*prev + curr
            else:
                number += curr
        else:
            number += curr

        prev = curr
    

    return number


print romanToInt('MCMLIV'.upper())
print romanToInt('MCMXC'.upper())
print romanToInt('MMXIV'.upper())
