# O(N^3) -- brutal force subset O(N^2) and isPalindrome O(N)
def longestPalindrome(s, n):

    if n == 0:
        return []

    longest = ''
    for i in xrange(len(s)+1-n):
                
        word = s[i:i+n]
        
        if isPalindrome(word) and len(longest) < len(word):
                longest = word

    temp = longestPalindrome(s, n-1)
        
    if len(longest) < len(temp):
        longest = temp

    return longest


def isPalindrome(s):

    return s == s[::-1]

# O(N^2)
def longestPalindrome2(s):

    left = 0
    right = 0 
    longest = ''
    for i in range(len(s)):
        
        left = i
        right = i + 1

        while isPalindrome(s[left:right+1]) and left >= 0 and right <= len(s):

            if len(longest) < len(s[left:right+1]):
                longest = s[left:right+1]
            left -= 1
            right += 1

    return longest
    

string = 'fffabbafgc'
print string

print longestPalindrome(string, len(string))
print longestPalindrome2(string)
