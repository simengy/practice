def divide(num1, num2):
    div = 0

    if num2 == 0:
        raise Exception('Divide Zero Error')
    elif num2 == 1:
        return num1, 0
    elif num1 < num2:
        return 0, num1

    div, mod = divide(num1 - num2, num2)
    div += 1

    return div, mod


#print divide(10, 0)

print divide(10, 2)

print divide(7, 3)

print divide(2, 8)
