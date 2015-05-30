def reverseInt(number):
    
    new = 0

    while number > 0:

        digit = number % 10
        number = number / 10
       
        # Overflow
        if (new * 10 + digit) / 10 == new:
            new = new * 10 + digit
        
    
    return new

print reverseInt(30448)
