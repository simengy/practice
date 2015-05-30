def revPolish(string):

    stack = []

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
        elif i == 'x':
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
    string = [5, 1, 2, '+', 4, 'x', '+', 3, '-']
    print revPolish(string)
