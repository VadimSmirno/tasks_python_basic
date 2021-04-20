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


def treatment(sig,num1,num2,lst):

    if len(lst) != 3:
        raise Exception
        # TODO, предлагаю дописать при вызове ошибки нужный текст
        #  Пример Exception("Текст ошибки")
        #  В таком случае, сможем ловить ошибки группой =)
    elif sig not in ['+', '-', '/', '*', '//', '%']:
        raise ArithmeticError
    elif not num1.isdigit() or not num2.isdigit():
        raise TypeError

sum_result = 0
calc = open('calc.txt', 'r')
count = 0
for i_elem in calc:
    # TODO, можно сразу создать 3 переменные, без применения индексов
    #  Пример a, b, c = [1, 2, 3]
    lst = i_elem.split()
    count += 1
    try:
        num1 = lst[0]
        sig = lst[1]
        num2 = lst[2]


        treatment(sig,num1,num2,lst)
        sum_result += define_sig(sig,int(num1),int(num2))
    # TODO, предлагаю попробовать ловить ошибки группой =)
    except ZeroDivisionError:
        print(f'Ошибка в {count} строке, на ноль делить нельзя')
    except ArithmeticError:
        print(f'Ошибка в {count} строке не арифметический знак')
    except TypeError:
        print (f'Ошибка в {count} строке символ не является числом')
    except Exception:
        print(f'Ошибка в {count} строке')
print(sum_result)
calc.close()
