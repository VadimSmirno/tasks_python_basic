# TODO, к 05 заданию актуальны и в этом.

def define_sig (sig,num1,num2):
    if sig in ['+','-','/','*','//','%']:
        if sig == '+':
            return num1 + num2
        if sig == '-':
            return num1 - num2
        if sig == '*':
            return num1 * num2
        if sig == '/':
            return num1 / num2
        if sig == '//':
            return num1 // num2
        if sig == '%':
            return num1 % num2
    else:
        raise ArithmeticError
def treatment(line):

    lst = line.split()
    num1 = int(lst[0])
    sig = lst[1]
    num2 = int(lst[2])
    if len(lst) != 3:
        raise Exception
    return define_sig(sig,num1,num2)

sum_result = 0
result = 0
caic = open('calc.txt', 'r')
count = 0
for i_elem in caic:
    count +=1
    try:
        sum_result += treatment(i_elem)
    except Exception:
        print('Ошибка в {0} строке: "{1}" на ноль делить нельзя. Хотите исправить?'.format(count,i_elem.rstrip('\n')))
        answer = input().lower()
        if answer == 'да':
            new_string = input('Введите исправленную строку:')
            sum_result += treatment(new_string)

print (sum_result)

caic.close()
