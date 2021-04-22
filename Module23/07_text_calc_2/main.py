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
    if len(lst) != 3 \
            or sig not in ['+', '-', '/', '*', '//', '%'] \
            or not num1.isdigit() \
            or not num2.isdigit():
        raise Exception('Строка не соответствует требованиям')


sum_result = 0
result = 0
calc = open('calc.txt', 'r')
count = 0
for i_elem in calc:
    lst = i_elem.split()
    count += 1
    try:
        num1, sig, num2 = lst
        treatment(sig, num1, num2, lst)
        sum_result += define_sig(sig, int(num1), int(num2))
    except Exception:
        print('Ошибка в {0} строке: "{1}":  Хотите исправить?'.format(count, i_elem.rstrip('\n')))
        answer = input().lower()
        if answer == 'да':
            new_string = input('Введите исправленную строку:').split()
            sum_result += define_sig(new_string[1], int(new_string[0]), int(new_string[2]))

print(sum_result)
calc.close()

# зачёт!
