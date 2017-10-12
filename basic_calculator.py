# Basic calculator

# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces. The integer division should truncate toward zero.


def sum_streaming(stream):
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


def basic_calulator_v1(stream):
    N = len(stream)

    digits = []
    operators = []
    number = ''

    sum = 0
    is_bracket = 0

    for i in xrange(N):
        # scan through the expression and create two stacks:
        # operators and digits
        if stream[i] >= '0' and stream[i] <= '9':
            number += stream[i]
            if i == N - 1:
                digits.append(int(float(number)))
        else:
            if stream[i] == '(':
                is_bracket += 1
            if number != '':
                digits.append(int(float(number)))

            operators.append(stream[i])
            number = ''

        # pop the elements if meeting ')'
        if stream[i] == ')':
            tmp_op = operators.pop()
            tmp_sum = digits.pop()

            while tmp_op != '(' and operators:

                tmp_op = operators.pop()
                if digits:
                    tmp_num = digits.pop()
                else:
                    tmp_num = None

                if tmp_op == '+':
                    tmp_sum += tmp_num
                elif tmp_op == '-':
                    tmp_sum = tmp_num - tmp_sum
                elif tmp_op == '(' and tmp_num:
                    digits.append(tmp_num)

            if tmp_op == '(':
                digits.append(tmp_sum)
                is_bracket -= 1

    sum = digits.pop()
    while digits:
        tmp_num = digits.pop()
        tmp_op = operators.pop()
        if tmp_op == '+':
            sum += tmp_num
        elif tmp_op == '-':
            sum -= tmp_num

    return sum


stream_instance = [1, '+', 4, '*', 7, '*', 13, '-', 22]
print sum_streaming(stream_instance)

stream_instance = list('(1+(4+5+2)-3)+(6+8)')
print basic_calulator_v1(stream_instance)

stream_instance = list('9+8')
print basic_calulator_v1(stream_instance)
