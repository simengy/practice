def sum_streaming(stream, index, sum):
    assert len(stream) > 0, 'empty stream!'

    if index == len(stream) - 1:
        if stream[index - 1] == '*':
            return stream[index - 2] * stream[index]
        else:
            return stream[index]

    sum = stream[index]
    if stream[index + 1] == '*':
        tmp = stream[index] * stream[index + 2]
        sum + sum_streaming(stream, index + 2, sum)
    elif stream[index + 1] == '+':
        print sum, index, len(stream)
        sum = sum_streaming(stream, index, sum) + sum_streaming(stream, index + 2, sum)

    return sum


stream_instance = [1, '*', 4, '*', 7, '*', 13]

print sum_streaming(stream_instance, 0)
