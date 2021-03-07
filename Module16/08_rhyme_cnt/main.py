number_people = int(input('Количество человек: '))
number = int(input('Какое число в считалке: '))
print('\nЗначит выбывает каждый ', number, 'человек')


people = []


people.extend(list(range(1, number_people + 1)))
# TODO, по идее, эти вычисления должны быть тоже в цикле =)
#  Возможно будет удобнее использовать цикл while с условием.
list_length = number % len(people)
print('Текущий круг людей: ', people)
print('Начало счета c номера 1')
print('Выбывает человек под номером: ', people[list_length - 1])

for index in range(number_people - 1):
    list_length = number % len(people)
    print('\nТекущий круг людей: ', people)
    print('Начало счета c номера 1')
    print('Выбывает человек под номером: ', people[list_length - 1])
    people.remove(people[list_length - 1])

print('\nОстался человек под номером', people)
