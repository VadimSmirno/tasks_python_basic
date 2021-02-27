

def reverse_number(n,NUM):
    fractional_part = ''
    whole_part = ''
    new_number = ''

    for symbol in  (n):
        new_number = symbol + new_number

    for symbol in (n):
        if symbol != '.':
            whole_part = symbol + whole_part
        else:
            break
    for symbol in (new_number):
        if symbol != '.':
            fractional_part = fractional_part +symbol
        else:
            break

    a = whole_part +'.'+fractional_part



    print (NUM,'число наоборот:',a)
    return  float (a)






n = input ('Введите первое число ')

n2 =  input ('Введите второе число ')
print (reverse_number(n,'Первое') + reverse_number( n2,'Второе'))


