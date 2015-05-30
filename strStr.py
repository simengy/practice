def strStr(str1, str2):

    start = None
    end = None

    n = len(str1)
    for i in range(len(str2)):
        if i+n-1 < len(str2):
            if str2[i:i+n] == str1:
                return True

    return False

print strStr('asb', 'asbccc')

