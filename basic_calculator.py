# Basic calculator

# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces. The integer division should truncate toward zero.


def sum_streaming(stream, index):
    assert len(stream) > 0, 'empty stream!'

    N = len(stream)

    digits = []
    operators = []

    for i in xrange(N):
        if i % 2 == 0:
            digits.append(stream[i])
        else:
            operators.append(stream[i])

    M = len(operators)

    i = 0
    while i < M:
        if operators[i] == '*' and digits[i + 1]:
            digits[i] = digits[i] * digits[i + 1]
            del operators[i]
            del digits[i + 1]
            M -= 1
        else:
            i += 1

    sum = digits[0]
    for i in xrange(len(operators)):
        if operators[i] == '+':
            sum += digits[i + 1]
        else:
            sum -= digits[i + 1]

    return sum


stream_instance = [1, '+', 4, '*', 7, '*', 13, '-', 22]

print sum_streaming(stream_instance, 0)
