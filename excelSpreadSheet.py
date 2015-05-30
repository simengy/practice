import sys


DEBUG = 0

class graph:
    
    def __init__(self):
        self.table = []
        self.visit = []
        self.rows = 0
        self.cols = 0

    def tableLoad(self):
        
        total = 0
        temp = []

        for count, line in enumerate(sys.stdin):
        
            total = count
        
            if DEBUG: 
                print count, line

            if count == 0:
                cols, rows = line.rstrip('\n').split()
                self.cols, self.rows = int(cols), int(rows)
            else:
                if count % self.cols == 1:
                    temp = []
                temp.append(line)

                if count % self.cols == 0:
                    self.table.append(temp)
            
        assert self.rows * self.cols == total
        
        # init visit matrix
        for i in self.table:
            self.visit.append([False] * len(i))

    # convert number, RPN and column name to RPN
    # the spreadsheet is a graph, and the cyclic loop in the graph need to be checked
    def convertor(self, input):
    
        words = input.split()
        new = []

        for i in xrange(len(words)):
        
            # category: 0-operator, 1-number, 2-column
            number = None
        
            if words[i] == '+' or words[i] == '-' or words[i] == '*' or words[i] == '/':
                number = 0
                new.append(words[i])
            elif ord(words[i][0]) - ord('A') >= 0 and ord(words[i][0]) - ord('A') < 26:
                number = 2
            else:
                try:
                    if words[i][0] == '-':
                        sign = -1
                        words[i] = words[i][1:]
                    else:
                        sign = 1

                    words[i] = int(words[i]) * sign
                except:
                    ValueError('This is an illegal input')

                new.append(words[i])

            if number == 2:
                row = ord(words[i][0]) - ord('A')
                col = int(words[i][1:]) - 1
                    
                try:
                    if self.visit[row][col] == True:
                        
                        if DEBUG:
                            print >> sys.stderr, '\nWarning:\nLoop Detected in the graph!\n'
                        return None
                    
                    pos = self.table[row][col]
                    self.visit[row][col] = True
                except:
                    IndexError('The index is out of bound!')
                
                element = self.convertor(pos)
                
                # loop in DAC
                if element is None:
                    return None
                self.visit[row][col] = False
                new.extend(element)
                
        return new
    
    # evaluate RPN
    def RPN(self, string):

        stack = []

        if string is None:
            
            if DEBUG: 
                raise ValueError('Found loop in the graph!') 
            else:
                print >> sys.stderr, '\nWarning:\nFound Loop here!'
                return None
            
        for i in string:
        
            stack.append(i)

            if i == '+':
                stack.pop()
                a = float(stack.pop())
                b = float(stack.pop())
                stack.append(b + a)
            elif i == '-':
                stack.pop()
                a = float(stack.pop())
                b = float(stack.pop())
                stack.append(b - a)
            elif i == '*':
                stack.pop()
                a = float(stack.pop())
                b = float(stack.pop())
                stack.append(b * a)
            elif i == '/':
                stack.pop()
                a = float(stack.pop())
                b = float(stack.pop())
                stack.append(b / a)
                
        return stack
    

if __name__ == '__main__':

    excel = graph()
    
    excel.tableLoad()

    for row in excel.table:
        for line in row:
            
            if DEBUG:
                print '\n\n################################################'
                print 'Input Value = ', line
            
            expression = excel.convertor(line.rstrip('\n'))
            
            if DEBUG:
                print 'Converted expression = ', expression
                print 'RPN Evaluation value = ' 
            
            val = excel.RPN(expression)
            
            if val:
                if len(val) == 1:
                    print ('%.5f' % val[0])
                elif len(val) > 1:
                    print val
            else:
                print None
