class solution:

    def simplifyPath(self, path):

        levels = path.split('/')

        newPath = []
        for f in levels:
            if f == '':
                continue
            elif f == '.':
                continue
            elif f == '..':
                newPath.pop()    
            else:
                newPath.append(f)
                
        return newPath


path = '/a/./b/../c/'
#path = '/home/'
sol = solution()
print '/'.join(sol.simplifyPath(path))
