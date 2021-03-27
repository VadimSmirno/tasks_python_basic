max_number = int(input('Введите максимальное число: '))
numbers = input('Нужное число есть среди вот этих чисел: ')
result_set_number = set()


while numbers != 'Помогите!' or len(result_set_number) == 1:


    set_number = {i_num for i_num in numbers.split() if int(i_num) < max_number}
    answer = input('Ответ Артема: ').lower()
    print(set_number)
    if answer == 'да':
        result_set_number.update(set_number)
        print(result_set_number)
    elif answer ==  'нет':
        result_set_number -= set_number
        print(result_set_number)
    set_number = set()
    numbers = input('Нужное число есть среди вот этих чисел: ')


print ('Артём мог загадать следующие числа: ', end='')
for i_result in result_set_number:
    print (i_result, end='')

