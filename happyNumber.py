class Solution:

    def isHappy(self, n):
        
        string = []
        
        while n > 0:
            
            string.append(str(n%10))
            n = n / 10
        
        newN = 0
        for i in string:

            newN += int(i)**2

        if newN == 1:
            return True
        elif newN < 10:
            return False
        else:
            if self.isHappy(newN) == 1:
                return True
        

s = Solution()
print 'The answer is:', s.isHappy(19)
print 'The answer is:', s.isHappy(25)
