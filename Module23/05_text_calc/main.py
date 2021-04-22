def define_sig(sig, num1, num2):
    if sig == '+':
        return num1 + num2
    elif sig == '-':
        return num1 - num2
    elif sig == '*':
        return num1 * num2
    elif sig == '/':
        return num1 / num2
    elif sig == '//':
        return num1 // num2
    elif sig == '%':
        return num1 % num2


def treatment(sig, num1, num2, lst):
    if len(lst) != 3:
        raise Exception('Ошибка, в строке должно быть 3 символа')
    elif sig not in ['+', '-', '/', '*', '//', '%']:
        raise ArithmeticError('символ не арифметический')
    elif not num1.isdigit() or not num2.isdigit():
        raise TypeError('символы не являются числом')


sum_result = 0
calc = open('calc.txt', 'r')
count = 0
for i_elem in calc:
    lst = i_elem.split()
    count += 1
    try:
        num1, sig, num2 = lst
        treatment(sig, num1, num2, lst)
        sum_result += define_sig(sig, int(num1), int(num2))

    except (ArithmeticError, Exception, TypeError) as err:
        print(f'Ошибка в {count} строке {err}')
print(sum_result)
calc.close()

# зачёт!
