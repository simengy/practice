def validPalindrome(string):

    string = string.rstrip()
    string = string.replace(' ', '')
    string = string.lower()

    new = ''
    for i in string:
        if ord(i) < ord('a')  or ord(i) > ord('z') :
            continue
        new += i
    
    print new
    if new == rev(new):
        return True
    else:
        return False

def rev(string):

    if len(string) == 1 or len(string) == 0:
        return string
    
    new = rev(string[1:]) + string[0]

    return new


string = 'race a car'
string = 'A man, a plan, a canal:Panama'

print validPalindrome(string)
