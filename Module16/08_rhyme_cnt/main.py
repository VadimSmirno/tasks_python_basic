number_people = int(input('Количество человек: '))
number = int(input('Какое число в считалке: '))
print('\nЗначит выбывает каждый ', number, 'человек')


people = []


people.extend(list(range(1, number_people + 1)))


# TODO list_length на первую итерацию цикла равняется "2".
#  А по идее должны начинать с 0. Вычисления "list_length - 2" немного похожи на "костыль" в коде.
#  Предлагаю создать дополнительную переменную с изначальным значением равным "0".
#  Возможно её же можно будет использовать для расчёта индекса для удаления.
# TODO, предлагаю создать дополнительную переменную для расчёта индекса элемента, который необходимо удалить.
count = 0
while len(people) != 1:
    list_length = number % len(people)
    print('\nТекущий круг людей: ', people)
    print('Начало счета c номера',people[count] )
    print('Выбывает человек под номером: ', people[count])
    count += 1
    people.remove(people[count])

print('\nОстался человек под номером', people)
