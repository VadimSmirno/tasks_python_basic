def reverse_number(n, NUM):
    fractional_part = ''
    whole_part = ''
    new_number = ''

    for symbol in (n):
        new_number = symbol + new_number

    for symbol in (n):
        if symbol != '.':
            whole_part = symbol + whole_part
        else:
            break
    for symbol in (new_number):
        if symbol != '.':
            fractional_part = fractional_part + symbol
        else:
            break

    whole_part_fractional_part = whole_part + '.' + fractional_part

    print(NUM, 'число наоборот:', whole_part_fractional_part)
    return float(whole_part_fractional_part)


number1 = input('Введите первое число ')

number2 = input('Введите второе число ')
print('Сумма чисел "наоборот"', reverse_number(number1, 'Первое') + reverse_number(number2, 'Второе'))


