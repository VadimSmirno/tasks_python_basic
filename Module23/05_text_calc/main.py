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
    elif sig not in ['+', '-', '/', '*', '//', '%']:
        raise ArithmeticError
    elif not num1.isdigit() or not num2.isdigit():
        raise TypeError

sum_result = 0
calc = open('calc.txt', 'r')
count = 0
for i_elem in calc:
    lst = i_elem.split()
    count += 1
    try:
        num1 = lst[0]
        sig = lst[1]
        num2 = lst[2]


        treatment(sig,num1,num2,lst)
        sum_result += define_sig(sig,int(num1),int(num2))
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
