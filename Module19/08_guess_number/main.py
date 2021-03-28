max_number = int(input('Введите максимальное число: '))
numbers = ''
result_set_number = {num for num in range(1, max_number+1)}


while numbers != 'Помогите!':
    numbers = input('Нужное число есть среди вот этих чисел: ')
    set_numbers = {int(i_num) for i_num in numbers.split()}
    answer = input('Ответ Артема: ').lower()
    if answer == 'да':
        result_set_number = set_numbers.intersection(result_set_number)

    elif answer ==  'нет':
        result_set_number -= set_numbers

    if len(result_set_number) == 1:
        break



print ('Артем мог загадать следующие числа: ', end='')
for i_result in result_set_number:
    print (i_result, end=' ')

