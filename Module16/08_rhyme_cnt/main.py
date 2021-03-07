number_persons = int (input('Количество человек: '))
number = int(input('Какое число в считалке? '))
print ('Значит выбывает каждый ',number, 'человек')
list_number_persons = []
list_number_persons.extend((list(range(1,number_persons+1))))
number = 6
idx = number
print('Текущий круг людей', list_number_persons)
print ('Начало счета с номера 1')
while len(list_number_persons) > 1:
    if idx + 1 > len(list_number_persons):
        idx %= len(list_number_persons)
        print('Выбывает человек под номером',list_number_persons.pop(idx))
        idx = (idx + number) % len(list_number_persons)
print ('Остался человек под номером', list_number_persons[0])











