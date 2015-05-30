def checkVersion(versions):

    N  = len(versions)
    for i in range(N-1):
        for j in range(i+1, N):

            if comparison(versions[i], versions[j]) == 1:
                temp = versions[i]
                versions[i] = versions[j]
                versions[j] = temp

    return versions

def comparison(version1, version2):

    major1, minor1 = version1.split('.')
    major2, minor2 = version2.split('.')
    major1 = int(major1)
    major2 = int(major2)
    minor1 = int(minor1)
    minor2 = int(minor2)
    
    if major1 > major2:
        return 1
    elif major1 < major2:
        return 0
    else:
        if minor1 > minor2:
            return 1
        else:
            return 0

versions = ['3.1', '3.121', '1.23', '1.55', '2.32']

print checkVersion(versions) 
