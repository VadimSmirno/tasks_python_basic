number_people = int(input('Количество человек: '))
number = int(input('Какое число в считалке: '))
print('\nЗначит выбывает каждый ', number, 'человек')
people = []

people.extend(list(range(1, number_people + 1)))

count = 0

while len(people) != 1:

    print('\nТекущий круг людей: ', people)
    print('Начало счета c номера',people[count])
    loser_index = (count + number - 1) % len(people)
    print('Выбывает человек под номером: ', people[loser_index])
    people.remove(people[loser_index])
    if loser_index < len(people):
        count = loser_index
    else:
        count = 0

print('\nОстался человек под номером', people)
