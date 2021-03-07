skate_size_list = []
foot_size_list = []
count = 0
number_skates = int(input('Количество коньков: '))


for i_number_skates in range(1, number_skates + 1):
    print('размер ', i_number_skates, 'пары: ', end='')
    skate_size = int(input())
    skate_size_list.append(skate_size)

number_people = int(input('\nКоличество людей: '))
for i_number_people in range(1, number_people + 1):
    print('Размер ноги', i_number_people, 'человека: ', end='')
    foot_size = int(input())
    foot_size_list.append(foot_size)


for index in foot_size_list:
    if index in skate_size_list:
        count += 1
        skate_size_list.remove(index)

print('Наибольшее количество людей которые могут взять коньки:', count)
