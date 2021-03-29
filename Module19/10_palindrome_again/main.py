def palindrome(string):
    elem_dict = {}
    for symbol in string:
        elem_dict[symbol] = elem_dict.get(symbol, 0) + 1

    count = 0
    for i_value in elem_dict.values():
        if i_value % 2 != 0:
            count += 1

    return count <= 1


string = input('Введите строку: ')
if palindrome(string):
    print('Можно сделать палиндром')
else:
    print('Нельзя сделать палиндром')

# зачёт!
